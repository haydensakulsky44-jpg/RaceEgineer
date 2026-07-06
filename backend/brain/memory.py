import json
from pathlib import Path

MEMORY_PATH = Path(__file__).parent.parent / "data" / "memory.json"


def load_memory():

    if not MEMORY_PATH.exists():
        return {}

    with open(MEMORY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(data):

    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def set_memory(user_id: str, key: str, value: str):

    data = load_memory()

    if user_id not in data:
        data[user_id] = {}

    data[user_id][key] = value

    save_memory(data)


def get_memory(user_id: str, key: str):

    data = load_memory()

    return data.get(user_id, {}).get(key)