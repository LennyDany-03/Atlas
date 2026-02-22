import threading
import time

def start_timer(seconds: int):
    def run():
        time.sleep(seconds)
        print(f"\n⏰ TIMER DONE: {seconds} seconds\n🧠 > ", end="")

    threading.Thread(target=run, daemon=True).start()
    return f"Timer started for {seconds} seconds"