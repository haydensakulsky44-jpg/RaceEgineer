memory_store = {}


def set_memory(user_id: str, key: str, value: str):

    if user_id not in memory_store:
        memory_store[user_id] = {}

    memory_store[user_id][key] = value


def get_memory(user_id: str, key: str):

    return memory_store.get(user_id, {}).get(key)