import os
from typing import Optional
from app.models.audio import AudioFile
from app.config import settings

class AudioService:
	def __init__(self):
		self.upload_dir = settings.upload_dir
		os.makedirs(self.upload_dir, exist_ok=True)

	def save_audio_file(self, file_name: str, file_bytes: bytes, uploaded_by: Optional[str] = None) -> AudioFile:
		file_path = os.path.join(self.upload_dir, file_name)
		with open(file_path, "wb") as f:
			f.write(file_bytes)
		file_size_mb = round(len(file_bytes) / (1024 * 1024), 2)
		audio_file = AudioFile(
			file_name=file_name,
			file_path=file_path,
			file_size_mb=file_size_mb,
			uploaded_by=uploaded_by
		)
		return audio_file
