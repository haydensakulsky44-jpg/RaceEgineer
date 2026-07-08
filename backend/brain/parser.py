def parse_message(message: str):

    message = message.lower()

    intent = {
        "setup": False,
        "circuit": None,
        "car": None
    }

    # --- détection setup ---
    if "setup" in message:
        intent["setup"] = True

    # --- détection voiture ---
    if "ferrari" in message:
        intent["car"] = "Ferrari"

    if "red bull" in message:
        intent["car"] = "Red Bull"

    # --- détection circuits ---
    circuits = ["imola", "monza", "spa"]
    for c in circuits:
        if c in message:
            intent["circuit"] = c

    return intent