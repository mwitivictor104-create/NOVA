import json
import os

HISTORY_FILE = "data/history.json"

def _ensure():
    os.makedirs("data", exist_ok=True)

def load_history():
    _ensure()

    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def add_message(role, content):
    history = load_history()

    history.append({
        "role": role,
        "content": content
    })

    _ensure()

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def clear_history():
    _ensure()

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)


def history_count():
    """Return the number of stored messages."""
    return len(load_history())
