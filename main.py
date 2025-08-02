import os
import sys
import argparse
from pathlib import Path

# Requisitos: pip install vosk moviepy
# Baixe o modelo de voz para português em: https://alphacephei.com/vosk/models
# Extraia o modelo em uma pasta chamada 'model' na raiz do projeto

import subprocess
from vosk import Model, KaldiRecognizer
import wave

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

    for video in selecionados:
        print(f"[INFO] Processando vídeo: {video.name}")
        audio_path = video.with_suffix('.wav')
        extract_audio(video, audio_path)
        if os.path.exists(audio_path):
            transcription = transcribe_audio(audio_path)
            save_markdown(transcription, cliente, video.name)
            print(f"[INFO] Arquivo de áudio mantido: {audio_path}")
        else:
            print(f"[ERRO] Não foi possível extrair o áudio. Pulando transcrição.")

if __name__ == "__main__":
    main()
