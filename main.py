import contextlib
import math

# Função para dividir áudio WAV em partes de até 1400 segundos
def split_wav(audio_path, max_seconds=1400):
    import wave
    import math
    parts = []
    with contextlib.closing(wave.open(str(audio_path), 'rb')) as wf:
        framerate = wf.getframerate()
        nframes = wf.getnframes()
        sampwidth = wf.getsampwidth()
        nchannels = wf.getnchannels()
        duration = nframes / float(framerate)
        total_parts = math.ceil(duration / max_seconds)
        for i in range(total_parts):
            start_frame = int(i * max_seconds * framerate)
            # O último segmento deve ir até o último frame
            if i == total_parts - 1:
                end_frame = nframes
            else:
                end_frame = int(min((i+1) * max_seconds * framerate, nframes))
            wf.setpos(start_frame)
            frames = wf.readframes(end_frame - start_frame)
            part_path = audio_path.parent / f"{audio_path.stem}_part{i+1}.wav"
            with wave.open(str(part_path), 'wb') as out:
                out.setnchannels(nchannels)
                out.setsampwidth(sampwidth)
                out.setframerate(framerate)
                out.writeframes(frames)
            print(f"[DEBUG] Parte {i+1}: frames {start_frame} até {end_frame} (total: {end_frame-start_frame})")
            parts.append(part_path)
    return parts
import os
import sys
import dotenv
from openai import OpenAI
import argparse
from pathlib import Path

# Requisitos: pip install vosk moviepy
# Baixe o modelo de voz para português em: https://alphacephei.com/vosk/models
# Extraia o modelo em uma pasta chamada 'model' na raiz do projeto

import subprocess
from vosk import Model, KaldiRecognizer
import wave
def transcribe_audio_openai(audio_path):
    import os
    from openai import OpenAI
    import wave
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("[ERRO] OPENAI_API_KEY não configurada no ambiente.")
        return None
    client = OpenAI(api_key=api_key)
    
    # Verificar duração do áudio e calcular custo
    with wave.open(str(audio_path), "rb") as wf:
        duration = wf.getnframes() / float(wf.getframerate())
    
    # Calculadora de custo (baseado em $0.006 por minuto do GPT-4o-mini)
    duration_minutes = duration / 60
    estimated_cost = duration_minutes * 0.006  # $0.006 por minuto
    
    print(f"\n💰 CALCULADORA DE CUSTO OPENAI")
    print(f"📊 Duração do áudio: {duration:.1f} segundos ({duration_minutes:.1f} minutos)")
    print(f"💵 Custo estimado: ${estimated_cost:.4f} USD (~R$ {estimated_cost * 5.5:.2f})")
    
    if duration > 1400:
        parts_needed = math.ceil(duration / 1400)
        print(f"⚠️  Áudio será dividido em {parts_needed} partes (limite: 1400s por parte)")
    
    confirm = input(f"\n🔄 Deseja prosseguir com a transcrição? [s/n]: ").strip().lower()
    if confirm != 's':
        print("❌ Transcrição cancelada pelo usuário.")
        return None
    
    if duration > 1400:
        print(f"[INFO] Áudio com {duration:.2f}s excede limite do OpenAI. Dividindo em partes...")
        parts = split_wav(audio_path, max_seconds=1400)
        full_transcript = ""
        print(f"[DEBUG] Total de partes criadas: {len(parts)}")
        
        for idx, part in enumerate(parts, 1):
            print(f"[INFO] Transcrevendo parte {idx}/{len(parts)}...")
            with open(part, "rb") as audio_file:
                try:
                    transcription = client.audio.transcriptions.create(
                        model="gpt-4o-mini-transcribe",
                        file=audio_file
                    )
                    part_text = transcription.text.strip()
                    print(f"[DEBUG] Parte {idx} - Caracteres transcritos: {len(part_text)}")
                    print(f"[DEBUG] Parte {idx} - Primeiros 100 chars: {part_text[:100]}...")
                    print(f"[DEBUG] Parte {idx} - Últimos 100 chars: ...{part_text[-100:]}")
                    
                    if part_text:  # Só adiciona se não estiver vazio
                        full_transcript += part_text + "\n\n"
                    else:
                        print(f"[AVISO] Parte {idx} resultou em transcrição vazia!")
                        
                except Exception as e:
                    print(f"[ERRO] Falha na transcrição da parte {idx}: {e}")
                    
        # Limpar arquivos temporários das partes
        for part in parts:
            try:
                os.remove(part)
            except Exception:
                pass
                
        print(f"[DEBUG] Transcrição final - Total de caracteres: {len(full_transcript)}")
        print("[INFO] Transcrição concluída via OpenAI (partes).")
        return full_transcript.strip()
    else:
        with open(audio_path, "rb") as audio_file:
            try:
                transcription = client.audio.transcriptions.create(
                    model="gpt-4o-mini-transcribe",
                    file=audio_file
                )
                print("[INFO] Transcrição concluída via OpenAI.")
                return transcription.text
            except Exception as e:
                print(f"[ERRO] Falha na transcrição via OpenAI: {e}")
                return None

BASE_DIR = Path(__file__).parent.resolve()
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
MODEL_DIR = BASE_DIR / "model"

def extract_audio(video_path, audio_path):
    # Extrai áudio usando ffmpeg (precisa estar instalado no sistema)
    cmd = [
        "ffmpeg",
        "-y",  # overwrite output
        "-i", str(video_path),
        "-vn",  # no video
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        str(audio_path)
    ]
    print(f"[INFO] Extraindo áudio do vídeo para arquivo WAV...")
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Mensagens do ffmpeg ocultas
    except subprocess.CalledProcessError as e:
        print(f"[ERRO] Falha ao extrair áudio do vídeo: {e}")
    if os.path.exists(audio_path):
        print(f"[INFO] Áudio extraído com sucesso.")
    else:
        print(f"[ERRO] Arquivo de áudio não foi criado.")

def transcribe_audio(audio_path):
    import json
    log_path = OUTPUT_DIR / "transcricao-debug.log"
    if not MODEL_DIR.exists():
        msg = "Modelo Vosk não encontrado. Baixe e extraia em ./model"
        print(msg)
        with open(log_path, "a", encoding="utf-8") as log:
            log.write(msg + "\n")
        return ""
    print(f"[INFO] Iniciando transcrição do áudio...")
    try:
        wf = wave.open(str(audio_path), "rb")
        info = f"WAV channels: {wf.getnchannels()} | Sample width: {wf.getsampwidth()} | Frame rate: {wf.getframerate()} | Frames: {wf.getnframes()}"
        duration = wf.getnframes() / float(wf.getframerate())
        print(f"[INFO] Duração do áudio: {duration:.2f} segundos")
        with open(log_path, "a", encoding="utf-8") as log:
            log.write(f"Arquivo: {audio_path}\n{info}\nDuração: {duration:.2f} segundos\n")
    except Exception as e:
        msg = f"Erro ao abrir arquivo WAV: {e}"
        print(f"[ERRO] Erro ao abrir arquivo WAV: {e}")
        with open(log_path, "a", encoding="utf-8") as log:
            log.write(msg + "\n")
        return ""
    try:
        model = Model(str(MODEL_DIR))
    except Exception as e:
        msg = f"Erro ao carregar modelo Vosk: {e}"
        print(f"[ERRO] Erro ao carregar modelo Vosk: {e}")
        with open(log_path, "a", encoding="utf-8") as log:
            log.write(msg + "\n")
        return ""
    try:
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)
        results = []
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                res = rec.Result()
                results.append(res)
        results.append(rec.FinalResult())
        transcript = "\n".join([json.loads(r).get("text","") for r in results])
        print(f"[INFO] Transcrição concluída.")
        with open(log_path, "a", encoding="utf-8") as log:
            log.write(f"Transcrição: {transcript[:200]}...\n")
        return transcript
    except Exception as e:
        msg = f"Erro ao transcrever áudio: {e}"
        print(f"[ERRO] Erro ao transcrever áudio: {e}")
        with open(log_path, "a", encoding="utf-8") as log:
            log.write(msg + "\n")
        return ""

def save_markdown(transcription, client_name, video_file):
    output_file = OUTPUT_DIR / f"transcricao-de-reuniao-{client_name}.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Transcrição de Reunião - {client_name}\n\n")
        f.write(f"**Arquivo de origem:** {video_file}\n\n")
        f.write(transcription)
    print(f"Transcrição salva em: {output_file}")

def main():
    print("\n=== Transcrição de vídeos ===\n")
    # Carregar variáveis do .env se existir
    dotenv.load_dotenv()

    print("\n=== Transcrição de vídeos ===\n")
    print("Escolha o motor de transcrição:")
    print("[1] Vosk (offline)")
    print("[2] OpenAI GPT-4o (requer token)")
    metodo = input("Digite 1 ou 2: ").strip()
    usar_openai = metodo == "2"

    videos = list(INPUT_DIR.glob("*.mp4"))
    if not videos:
        print("Nenhum vídeo mp4 encontrado na pasta input/")
        sys.exit(1)

    print("Selecione os vídeos que deseja transcrever:")
    for idx, video in enumerate(videos, 1):
        print(f"[{idx}] {video.name}")
    escolha = input("Digite os números dos vídeos separados por vírgula (ex: 1,3): ").strip()
    indices = [int(i)-1 for i in escolha.split(",") if i.strip().isdigit() and 0 < int(i) <= len(videos)]
    selecionados = [videos[i] for i in indices]
    if not selecionados:
        print("Nenhum vídeo selecionado. Encerrando.")
        sys.exit(1)

    cliente = input("Digite o nome do cliente para nomear o arquivo de saída: ").strip()
    if not cliente:
        print("Nome do cliente não informado. Encerrando.")
        sys.exit(1)

    import shutil
    temp_dir = BASE_DIR / "temp"
    temp_dir.mkdir(exist_ok=True)
    temp_files = []
    for video in selecionados:
        print(f"[INFO] Processando vídeo: {video.name}")
        audio_path = temp_dir / f"{video.stem}.wav"
        extract_audio(video, audio_path)
        temp_files.append(audio_path)
        if os.path.exists(audio_path):
            if usar_openai:
                transcription = transcribe_audio_openai(audio_path)
                if transcription is None:
                    print("[ERRO] Não foi possível transcrever via OpenAI. Deseja tentar via Vosk? [s/n]")
                    if input().strip().lower() == "s":
                        transcription = transcribe_audio(audio_path)
                    else:
                        transcription = ""
            else:
                transcription = transcribe_audio(audio_path)
            save_markdown(transcription, cliente, video.name)
            print(f"[INFO] Arquivo de áudio mantido em: {audio_path}")
        else:
            print(f"[ERRO] Não foi possível extrair o áudio. Pulando transcrição.")

    # Limpeza automática da pasta temp (sempre executada)
    try:
        shutil.rmtree(temp_dir)
        print("[INFO] Pasta temp/ removida com sucesso.")
    except Exception as e:
        print(f"[ERRO] Falha ao remover pasta temp/: {e}")

if __name__ == "__main__":
    main()
