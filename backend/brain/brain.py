from backend.brain.router import route


def think(message: str, user_id: str):
    return route(message, user_id)