from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from .base import BaseModelWithId

class UserType(str, Enum):
	FREE = "free"
	PREMIUM = "premium"
	ADMIN = "admin"

class UserLimits(BaseModel):
	max_concurrent_vosk: int
	max_daily_vosk: int
	max_monthly_vosk: int
	max_concurrent_openai: int
	max_monthly_openai: int
	max_file_size_mb: int
	max_duration_minutes: int
	queue_priority: int

class User(BaseModelWithId):
	email: EmailStr
	username: str
	user_type: UserType = UserType.FREE
	permissions: List[str] = []
	limits: UserLimits
	is_active: bool = True
	hashed_password: str

class UserCreate(BaseModel):
	email: EmailStr
	username: str
	password: str
	user_type: UserType = UserType.FREE

class UserLogin(BaseModel):
	username: str
	password: str

class Token(BaseModel):
	access_token: str
	refresh_token: str
	token_type: str = "bearer"
	expires_in: int
	user_id: str
	user_type: UserType
	permissions: List[str]
	limits: UserLimits
