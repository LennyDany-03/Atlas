def analyze_intent(text: str):
    if text in ["exit", "quit"]:
        return {"intent": "exit"}

    if text.startswith("open"):
        return {"intent": "open_app"}

    if text.startswith("play"):
        return {"intent": "play_media"}

    return {"intent": "unknown"}