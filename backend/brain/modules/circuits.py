import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent.parent / "data" / "circuits.json"

with open(DATA_PATH, "r", encoding="utf-8") as file:
    circuits = json.load(file)


def handle(message: str):

    for circuit_name, infos in circuits.items():

        if circuit_name in message:

            tips = "\n".join(f"- {tip}" for tip in infos["tips"])

            return (
                f"📍 {circuit_name.title()}\n\n"
                f"Pays : {infos['country']}\n"
                f"Longueur : {infos['length_km']} km\n"
                f"Virages : {infos['corners']}\n\n"
                f"{infos['description']}\n\n"
                f"Conseils :\n{tips}"
            )

    return None