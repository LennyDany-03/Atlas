import webbrowser

def open_url(url: str):
    try:
        webbrowser.open(url)
        return f"Opened URL: {url}"
    except Exception as e:
        return f"Failed to open URL: {e}"