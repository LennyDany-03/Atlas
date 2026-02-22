import subprocess
import platform

def open_app(name: str):
    """
    Open applications reliably on Windows using Start Menu
    """
    try:
        if platform.system() == "Windows":
            subprocess.Popen(
                f'start "" "{name}"',
                shell=True
            )
            return f"Application '{name}' opened"
        return "Unsupported OS"
    except Exception as e:
        return f"Failed to open app '{name}': {e}"


def close_app(process_name: str):
    """
    Close an application by process name (Windows)
    Example: close_app("brave.exe"), close_app("spotify.exe")
    """
    try:
        if platform.system() == "Windows":
            subprocess.run(
                ["taskkill", "/f", "/im", process_name],
                capture_output=True,
                text=True
            )
            return f"Application '{process_name}' closed"
        return "Unsupported OS"
    except Exception as e:
        return f"Failed to close app '{process_name}': {e}"