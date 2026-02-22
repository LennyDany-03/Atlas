import os

def read_file(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Failed to read file: {e}"


def write_file(path: str, content: str):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"File written: {path}"
    except Exception as e:
        return f"Failed to write file: {e}"


def delete_file(path: str):
    try:
        os.remove(path)
        return f"File deleted: {path}"
    except Exception as e:
        return f"Failed to delete file: {e}"