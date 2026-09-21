"""
NOVA Local AI
"""

from ai_engine import engine


def local_ai(prompt):

    return f"NOVA received: {prompt}"


engine.register(
    "local",
    local_ai
)
