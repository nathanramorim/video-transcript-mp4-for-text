from pydantic import BaseModel, Field
from typing import Optional
from .base import BaseModelWithId

class TranscriptionJob(BaseModelWithId):
	file_name: str
	client_name: Optional[str] = None
	user_id: Optional[str] = None
	method: str = "vosk"
	file_size_mb: Optional[float] = None
	status: str = "queued"
	result_path: Optional[str] = None
	error: Optional[str] = None
