from fastapi import APIRouter, UploadFile, File, HTTPException
from app.models.transcription import TranscriptionJob
from app.services.vosk_service import VoskService

router = APIRouter(prefix="/vosk", tags=["Vosk Transcription"])

@router.post("/transcribe")
async def transcribe_vosk(video_file: UploadFile = File(...)):
	# Validação simples
	if video_file.content_type not in ["video/mp4", "video/quicktime"]:
		raise HTTPException(400, "Tipo de arquivo não suportado")
	file_bytes = await video_file.read()
	job = TranscriptionJob(file_name=video_file.filename, file_size_mb=len(file_bytes)/(1024*1024))
	vosk_service = VoskService()
	result = vosk_service.transcribe(job, video_bytes=file_bytes)
	return result
