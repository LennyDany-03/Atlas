import subprocess

ALLOWED_COMMANDS = ["dir", "echo", "ipconfig", "whoami"]

def run_command(command: str):
    """
    Run restricted shell commands only
    """
    base_cmd = command.split()[0].lower()

    if base_cmd not in ALLOWED_COMMANDS:
        return f"Command '{base_cmd}' is not allowed"

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Shell command failed: {e}"