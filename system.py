import platform
import sys

def status():
    return {
        "python": sys.version.split()[0],
        "platform": platform.system(),
        "machine": platform.machine(),
    }

def status_text():
    info = status()

    return (
        "NOVA system online\n"
        f"Python: {info['python']}\n"
        f"Platform: {info['platform']}\n"
        f"Architecture: {info['machine']}"
    )
