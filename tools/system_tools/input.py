import pyautogui

def press_key(key: str):
    try:
        pyautogui.press(key)
        return f"Key '{key}' pressed"
    except Exception as e:
        return f"Failed to press key: {e}"


def type_text(text: str):
    try:
        pyautogui.write(text, interval=0.05)
        return "Text typed successfully"
    except Exception as e:
        return f"Failed to type text: {e}"


def mouse_click(x: int, y: int):
    try:
        pyautogui.click(x, y)
        return f"Mouse clicked at ({x}, {y})"
    except Exception as e:
        return f"Mouse click failed: {e}"