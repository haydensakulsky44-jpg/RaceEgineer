def think(message: str):

    message = message.lower()

    if any(word in message for word in ["bonjour", "salut", "hello"]):
        return (
            "Bonjour ! Je suis RaceEngineer. "
            "Comment puis-je t'aider aujourd'hui ?"
        )

    elif any(word in message for word in ["setup", "réglage", "reglage"]):
        return (
            "Pour quel jeu, quelle voiture et quel circuit souhaites-tu un setup ?"
        )

    elif any(word in message for word in ["imola"]):
        return (
            "Imola est un circuit très technique. Les sorties de Tamburello, Piratella et Acque Minerali sont déterminantes."
        )

    elif any(word in message for word in ["telemetrie", "télémétrie"]):
        return (
            "Je pourrai bientôt analyser des fichiers de télémétrie."
        )

    else:
        return (
            "Je n'ai pas encore appris ce sujet."
        )