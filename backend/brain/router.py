from backend.brain.modules.general import greeting
from backend.brain.modules.setup import setup
from backend.brain.modules.telemetry import telemetry
from backend.brain.modules import circuits

from backend.brain.memory import set_memory, get_memory


def route(message: str, user_id: str):

    message = message.lower()
    responses = []

    # 🧠 Mémoire simple (ex: voiture)
    if "je roule en" in message:
        car = message.replace("je roule en", "").strip()
        set_memory(user_id, "car", car)
        return f"Ok, je retiens que tu roules en {car}"

    # Greeting
    if any(word in message for word in ["bonjour", "salut", "hello"]):
        responses.append(greeting())

    # Setup
    if any(word in message for word in ["setup", "réglage", "reglage"]):
        car = get_memory(user_id, "car")
        if car:
            responses.append(f"Tu roules en {car}. Parlons setup.")
        responses.append(setup())

    # Telemetry
    if any(word in message for word in ["telemetrie", "télémétrie"]):
        responses.append(telemetry())

    # Circuits
    circuit_response = circuits.handle(message)
    if circuit_response:
        responses.append(circuit_response)

    if not responses:
        return "Je n'ai pas encore appris ce sujet."

    return "\n\n".join(responses)