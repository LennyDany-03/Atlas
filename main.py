from interface.cli.input import get_cli_input
from interface.cli.normalizer import normalize_input
from interface.cli.output import render_output
from agent.core import agent_core

def main():
    print("🧠 AI Agent CLI started. Type 'exit' to quit.\n")

    while True:
        raw_input = get_cli_input()
        normalized = normalize_input(raw_input)

        response = agent_core(normalized)
        render_output(response)

        if response.get("exit"):
            break

if __name__ == "__main__":
    main()