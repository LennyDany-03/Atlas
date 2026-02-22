from llm.client import call_llm
from llm.prompts import build_prompt
from llm.parser import parse_llm_output
from tools.registry import execute_tool

def agent_core(normalized_input: dict):
    text = normalized_input["content"]

    if text.lower() in ["exit", "quit"]:
        return {"message": "Shutting down agent.", "exit": True}

    prompt = build_prompt(text)
    raw = call_llm(prompt)
    data = parse_llm_output(raw)

    result = execute_tool(data.get("tool"))

    return {
        "message": (
            f"Intent: {data.get('intent')}\n"
            f"Goal: {data.get('goal')}\n"
            f"Result: {result}"
        ),
        "exit": False
    }