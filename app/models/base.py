from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import uuid

class BaseModelWithId(BaseModel):
	id: str = Field(default_factory=lambda: str(uuid.uuid4()))
	created_at: datetime = Field(default_factory=datetime.utcnow)
	updated_at: Optional[datetime] = None

class ResponseModel(BaseModel):
	success: bool = True
	message: str = "Success"
	data: Optional[dict] = None
	timestamp: datetime = Field(default_factory=datetime.utcnow)
