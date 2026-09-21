# ==========================================================
# NOVA AI INTERFACE
# Connects main.py to NOVA's existing brain
# ==========================================================

try:
    from brain import ask as brain_ask
except Exception as e:
    brain_ask = None
    brain_error = str(e)


class NovaAI:

    def __init__(self):
        self.name = "NOVA"
        self.owner = "Boss Victor"

    def respond(self, command):

        command = command.strip()

        if not command:
            return ""

        lower = command.lower()

        # Basic identity commands
        if lower in ["hello", "hi", "hey", "hello nova", "hi nova"]:
            return "Hello Boss Victor. How can I help you?"

        if "who are you" in lower or "what is your name" in lower:
            return "I am NOVA, your AI assistant."

        if "who is my owner" in lower or "who owns you" in lower:
            return "My owner is Boss Victor."

        # Existing NOVA brain
        if brain_ask:

            try:
                result = brain_ask(command)

                if result is not None:
                    return str(result)

            except Exception as e:
                return f"NOVA brain error: {e}"

        return "NOVA brain is currently unavailable."
