from fastapi import FastAPI
from pydantic import BaseModel

from backend.brain.brain import think

app = FastAPI()

RACEENGINEER_NAME = "RaceEngineer"
VERSION = "0.3"


class ChatRequest(BaseModel):
    message: str
    user_id: str = "default"


@app.get("/status")
def status():
    return {
        "status": "online",
        "name": RACEENGINEER_NAME,
        "version": VERSION
    }


@app.post("/chat")
def chat(request: ChatRequest):

    response = think(request.message, request.user_id)

    return {
        "assistant": RACEENGINEER_NAME,
        "version": VERSION,
        "question": request.message,
        "response": response
    }