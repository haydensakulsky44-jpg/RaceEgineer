from fastapi import responses

from backend.brain.modules.general import greeting
from backend.brain.modules.setup import setup
from backend.brain.modules.telemetry import telemetry
from backend.brain.modules import circuits
from backend.brain.memory import set_memory, get_memory
from backend.brain.parser import parse_message

def route(message: str, user_id: str):
    intent = parse_message(message)
    message = message.lower()
    responses = {
    "circuit": None,
    "setup": None,
    "telemetry": None,
    "general": None,
}
    

    # 🧠 Mémoire simple (ex: voiture)
    if "je roule en" in message:
        car = message.replace("je roule en", "").strip()
        set_memory(user_id, "car", car)
        return f"Ok, je retiens que tu roules en {car}"

    # Greeting
    if any(word in message for word in ["bonjour", "salut", "hello"]):
        responses["general"] = greeting()

    # Setup
    # Setup intelligent (avec intent parser)
    if intent["setup"]:
        car = intent["car"] or get_memory(user_id, "car")
        circuit = intent["circuit"]

        if car and circuit:
            return f"Setup {car} pour {circuit} : priorité stabilité et traction."

        car_msg = f"Tu roules en {car}. " if car else ""
        responses["setup"] = car_msg + setup()

    # Telemetry
    if any(word in message for word in ["telemetrie", "télémétrie"]):
        responses["telemetry"] = telemetry()

    # Circuits
    circuit_response = circuits.handle(message)
    if circuit_response:
        responses["circuit"] = circuit_response

    ordered = []

    for key in ["circuit", "setup", "telemetry", "general"]:
        if responses[key]:
            ordered.append(responses[key])

    if not ordered:
        return "Je n'ai pas encore appris ce sujet."

    return "\n\n".join(ordered)

