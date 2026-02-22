from llm.client import call_llm
from llm.prompts import build_prompt
from llm.parser import parse_llm_output
from tools.registry import execute_tool

def agent_core(normalized_input: dict):
    user_text = normalized_input["content"]

    if user_text.lower() in ["exit", "quit"]:
        return {"message": "Shutting down agent.", "exit": True}

    # LLM reasoning
    prompt = build_prompt(user_text)
    raw_output = call_llm(prompt)
    llm_data = parse_llm_output(raw_output)

    next_action = llm_data["plan"][0]

    # Execute tool
    result = execute_tool(next_action)

    return {
        "message": (
            f"Intent: {llm_data['intent']}\n"
            f"Goal: {llm_data['goal']}\n"
            f"Action: {next_action}\n"
            f"Result: {result}"
        ),
        "exit": False,
        "debug": llm_data
    }