from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
	app_name: str = "Video Transcript API"
	app_version: str = "1.0.0"
	debug: bool = False
	api_host: str = "0.0.0.0"
	api_port: int = 8000
	# JWT
	jwt_secret_key: str
	jwt_algorithm: str = "HS256"
	jwt_access_token_expire_minutes: int = 60
	jwt_refresh_token_expire_days: int = 30
	# Redis
	redis_url: str = "redis://localhost:6379/0"
	# OpenAI
	openai_api_key: Optional[str] = None
	openai_max_seconds: int = 900
	openai_overlap_seconds: int = 15
	openai_transcribe_prompt: str = "Transcreva todo o conteúdo..."
	# Vosk
	vosk_model_path: str = "./model"
	# Storage
	temp_dir: str = "./storage/temp"
	upload_dir: str = "./storage/uploads"
	output_dir: str = "./storage/outputs"
	# Limits
	max_file_size_mb: int = 500
	max_duration_minutes: int = 120
	max_concurrent_vosk: int = 3
	# Queue
	queue_max_size: int = 50
	cleanup_interval_hours: int = 1
	# User limits
	free_daily_limit: int = 10
	free_concurrent_limit: int = 1
	premium_daily_limit: int = 50
	premium_concurrent_limit: int = 3

	class Config:
		env_file = ".env"

settings = Settings()
