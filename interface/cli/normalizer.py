from datetime import datetime

def normalize_input(text: str):
    return {
        "source": "cli",
        "type": "command",
        "content": text.lower(),
        "timestamp": datetime.utcnow().isoformat()
    }