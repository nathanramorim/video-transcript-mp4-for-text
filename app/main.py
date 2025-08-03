from fastapi import FastAPI
from app.routers.v1 import vosk, markdown

app = FastAPI()

app.include_router(vosk.router, prefix="/api/v1")
app.include_router(markdown.router, prefix="/api/v1")
