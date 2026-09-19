"""
NOVA Utility Functions
"""

from datetime import datetime


def current_time():
    """Return the current local time."""
    return datetime.now().strftime("%H:%M:%S")


def current_date():
    """Return the current local date."""
    return datetime.now().strftime("%Y-%m-%d")


def clean_text(text):
    """Clean and normalize user input."""
    if text is None:
        return ""

    return " ".join(str(text).strip().split())


def normalize_command(text):
    """Normalize a command for easier matching."""
    return clean_text(text).lower()


def format_number(value):
    """Format numbers neatly."""
    try:
        number = float(value)

        if number.is_integer():
            return str(int(number))

        return f"{number:.2f}"

    except (TypeError, ValueError):
        return str(value)


def safe_int(value, default=0):
    """Safely convert a value to an integer."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def safe_float(value, default=0.0):
    """Safely convert a value to a float."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return default
