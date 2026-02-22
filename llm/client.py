import subprocess

OLLAMA_MODEL = "minimax-m2.5:cloud"

def call_llm(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", OLLAMA_MODEL],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",     # ✅ FORCE UTF-8
        errors="ignore"       # ✅ SAFETY NET
    )

    if result.returncode != 0:
        return ""

    return result.stdout.strip()