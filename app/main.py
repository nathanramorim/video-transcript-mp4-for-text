from fastapi import FastAPI
from app.routers.v1 import vosk

app = FastAPI()

app.include_router(vosk.router, prefix="/api/v1")
