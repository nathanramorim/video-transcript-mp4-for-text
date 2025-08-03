from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse
from app.services.vosk_service import VoskService
from app.services.openai_service import OpenAIService
import tempfile
import shutil
import os
from datetime import datetime

router = APIRouter(prefix="/markdown", tags=["Markdown Generation"])

@router.post("/generate")
async def generate_markdown(
    video_file: UploadFile = File(...),
    prompt: str = Form(...),
    client_name: str = Form(...),
    persist: bool = Form(False)
):
    """
    Recebe vídeo, gera transcrição com Vosk, organiza markdown via GPT-4o mini.
    Retorna markdown para download. Se persist=True, salva em output/.
    """
    # 1. Salvar vídeo temporário
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        shutil.copyfileobj(video_file.file, temp_video)
        temp_video_path = temp_video.name

    # 2. Converter para WAV (temporário)
    vosk_service = VoskService()


    # Ler bytes do vídeo
    with open(temp_video_path, "rb") as f:
        video_bytes = f.read()

    # Criar job
    from app.models.transcription import TranscriptionJob
    job = TranscriptionJob(
        file_name=video_file.filename,
        client_name=client_name,
        user_id="mvp",
        method="vosk",
        file_size_mb=video_file.size / (1024 * 1024)
    )

    # Transcrever
    transcription_result = vosk_service.transcribe(job, video_bytes)
    transcription_text = transcription_result["result"]

    # 4. Gerar markdown via GPT-4o mini
    openai_service = OpenAIService()
    markdown_text = await openai_service.generate_markdown(transcription_text, prompt)

    # 5. Remover arquivos temporários
    try:
        os.remove(temp_video_path)
        os.remove(wav_path)
    except Exception:
        pass

    # 6. Persistir se solicitado
    if persist:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_dir = "storage/outputs"
        os.makedirs(output_dir, exist_ok=True)
        output_filename = f"{client_name}_{now}.md"
        output_path = os.path.join(output_dir, output_filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_text)
        return FileResponse(output_path, media_type="text/markdown", filename=output_filename)
    else:
        # Retornar markdown como download direto
        return StreamingResponse(
            iter([markdown_text]),
            media_type="text/markdown",
            headers={"Content-Disposition": f"attachment; filename={client_name}_transcription.md"}
        )
