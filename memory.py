import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "data", "memory.json")
HISTORY_FILE = os.path.join(BASE_DIR, "data", "history.json")


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_memory(memory):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=2, ensure_ascii=False)


def remember(key, value):
    key = str(key).strip()
    value = str(value).strip()
    if not key:
        return False
    memory = load_memory()
    memory[key] = value
    save_memory(memory)
    return True


def recall(key):
    return load_memory().get(str(key).strip())


def forget(key):
    key = str(key).strip()
    memory = load_memory()
    if key not in memory:
        return False
    del memory[key]
    save_memory(memory)
    return True


def all_memory():
    return load_memory()


# -----------------------------
# HISTORY LOG (new)
# -----------------------------

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except Exception:
        return []


def save_history(history):
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=2, ensure_ascii=False)


def log_event(category, description):
    """
    Record something NOVA did.
    category examples: 'lesson', 'analysis', 'quiz'
    """
    history = load_history()

    history.append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "category": str(category).strip(),
        "description": str(description).strip(),
    })

    save_history(history)
    return True


def get_history(category=None, limit=20):
    """
    Retrieve recent events, optionally filtered by category.
    """
    history = load_history()

    if category:
        history = [
            item for item in history
            if item.get("category") == category
        ]

    return history[-limit:]
