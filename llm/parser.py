import json
import re

def parse_llm_output(text: str):
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        data = json.loads(match.group())

        # Guarantee tool key exists
        if "tool" not in data:
            data["tool"] = None

        return data
    except Exception:
        return {
            "intent": "unknown",
            "goal": "clarify",
            "tool": None
        }