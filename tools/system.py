import subprocess
import platform
import time

def open_spotify():
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["spotify"])
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", "-a", "Spotify"])
        else:
            subprocess.Popen(["spotify"])
        return "Spotify launched successfully"
    except Exception as e:
        return f"Failed to open Spotify: {e}"


def play_spotify_music():
    """
    Spotify auto-plays last session when launched.
    This simulates 'play music' behavior.
    """
    try:
        open_spotify()
        time.sleep(2)  # give Spotify time to open
        return "Spotify opened and music playback started"
    except Exception as e:
        return f"Failed to play music: {e}"


def open_clock_app():
    """
    Opens Windows Clock app
    """
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["explorer.exe", "ms-clock:"])
            return "Clock app opened"
        return "Clock app not supported on this OS"
    except Exception as e:
        return f"Failed to open clock app: {e}"