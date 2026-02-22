# Permission levels: low, medium, high

RISK_LEVELS = {
    # apps
    "open_app": "low",
    "close_app": "medium",

    # browser
    "open_url": "low",

    # files
    "read_file": "medium",
    "write_file": "medium",
    "delete_file": "high",

    # shell
    "run_command": "high",

    # input (mouse/keyboard)
    "press_key": "medium",
    "type_text": "medium",
    "mouse_click": "high",

    # power
    "shutdown": "high",
    "restart": "high",
    "sleep": "high",
}

def check_permission(tool_name: str) -> bool:
    risk = RISK_LEVELS.get(tool_name, "high")

    if risk == "low":
        return True

    if risk == "medium":
        choice = input(f"⚠️ Allow '{tool_name}'? (y/n): ")
        return choice.lower() == "y"

    if risk == "high":
        choice = input(
            f"🚨 HIGH RISK ACTION '{tool_name}'\n"
            f"Type EXACTLY 'ALLOW' to continue: "
        )
        return choice == "ALLOW"

    return False