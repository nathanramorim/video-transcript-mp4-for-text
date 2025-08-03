import os
import tempfile
from app.models.transcription import TranscriptionJob
from moviepy.editor import VideoFileClip
from vosk import Model, KaldiRecognizer
import wave
import json

class VoskService:
	def __init__(self, model_path: str = "model"):
		self.model_path = model_path
		self.model = Model(model_path)

	def extract_audio(self, video_path: str) -> str:
		# Extrai áudio do vídeo e salva como WAV mono 16kHz temporário
		with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
			clip = VideoFileClip(video_path)
			if not clip.audio:
				raise ValueError("O vídeo enviado não possui faixa de áudio.")
			try:
				clip.audio.write_audiofile(temp_audio.name, fps=16000, nbytes=2, codec="pcm_s16le", ffmpeg_params=["-ac", "1"])
			except Exception as e:
				raise ValueError(f"Falha ao extrair áudio do vídeo: {e}")
			return temp_audio.name

	def transcribe(self, job: TranscriptionJob, video_bytes: bytes) -> dict:
		# Salva o arquivo recebido corretamente
		with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as temp_video:
			temp_video.write(video_bytes)
			temp_video_path = temp_video.name

		# Extrai áudio
		audio_path = self.extract_audio(temp_video_path)

		# Abre áudio para Vosk
		wf = wave.open(audio_path, "rb")
		if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in [16000, 44100]:
			raise ValueError("Áudio deve ser mono PCM 16bit 16kHz ou 44.1kHz")

		rec = KaldiRecognizer(self.model, wf.getframerate())
		results = []
		while True:
			data = wf.readframes(4000)
			if len(data) == 0:
				break
			if rec.AcceptWaveform(data):
				res = json.loads(rec.Result())
				results.append(res.get("text", ""))
		# Pega o texto final
		final_res = json.loads(rec.FinalResult())
		results.append(final_res.get("text", ""))
		transcript = " ".join(results).strip()

		# Limpeza dos arquivos temporários
		os.remove(temp_video_path)
		os.remove(audio_path)

		return {
			"job_id": job.id,
			"status": "completed",
			"result": transcript
		}
