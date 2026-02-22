import json
import re

def parse_llm_output(output: str):
    """
    Extract JSON safely from LLM output
    """
    try:
        match = re.search(r"\{.*\}", output, re.DOTALL)
        if not match:
            raise ValueError("No JSON found")

        return json.loads(match.group())
    except Exception:
        return {
            "intent": "unknown",
            "goal": "clarify_request",
            "plan": ["ask_user_for_clarification"]
        }