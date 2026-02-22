import re
from tools.system import open_spotify, play_spotify_music, open_clock_app
from tools.timer import start_timer

def execute_tool(action: str):
    action = action.lower()

    # 🎵 Spotify
    if "play" in action and "spotify" in action:
        return play_spotify_music()

    if "open spotify" in action or "spotify" in action:
        return open_spotify()

    # ⏱️ Timer (seconds)
    timer_match = re.search(r"(\d+)\s*(second|sec)", action)
    if timer_match:
        seconds = int(timer_match.group(1))
        open_clock_app()
        return start_timer(seconds)

    # ⏱️ Timer (minutes)
    minute_match = re.search(r"(\d+)\s*(minute|min)", action)
    if minute_match:
        seconds = int(minute_match.group(1)) * 60
        open_clock_app()
        return start_timer(seconds)

    return "No matching tool found for this action"