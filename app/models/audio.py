from pydantic import BaseModel, Field
from typing import Optional
from .base import BaseModelWithId

class AudioFile(BaseModelWithId):
	file_name: str
	file_path: str
	file_size_mb: float
	duration_seconds: Optional[float] = None
	uploaded_by: Optional[str] = None
	upload_time: Optional[str] = None
	transcription_id: Optional[str] = None
