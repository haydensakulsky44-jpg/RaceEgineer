from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
RACEENGINEER_NAME = "RaceEngineer"
VERSION = "0.2"

@app.get("/status")
def status():
    return {"status": "RaceEngineer backend is running"}
# ---- CHAT IA ----

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):

    message = request.message.lower()

    if any(word in message for word in ["bonjour", "salut", "hello"]):
        response = (
            "Bonjour ! Je suis RaceEngineer v0.2. "
            "Je peux t'aider en sport automobile, F1, endurance, GT3, prototypes, "
            "simracing, réglages et stratégie."
        )

    elif any(word in message for word in ["setup", "réglage", "reglage"]):
        response = (
            "Je peux t'aider à construire un setup. "
            "Indique-moi le jeu, la voiture et le circuit."
        )

    elif any(word in message for word in ["imola"]):
        response = (
            "Imola est un circuit très technique. Les vibreurs peuvent être agressifs et "
            "la précision est essentielle dans les variantes."
        )

    elif any(word in message for word in ["ferrari"]):
        response = (
            "Ferrari possède une immense histoire en compétition, en Formule 1 comme en endurance."
        )

    elif any(word in message for word in ["telemetrie", "télémétrie"]):
        response = (
            "Dans une future version, tu pourras m'envoyer un fichier de télémétrie afin que je l'analyse."
        )

    else:
        response = (
            "Je n'ai pas encore appris ce sujet. "
            "Je suis actuellement en développement."
        )

    return {
        "assistant": RACEENGINEER_NAME,
        "version": VERSION,
        "question": request.message,
        "response": response
    }