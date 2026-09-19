import re
from datetime import datetime


class NovaBrain:

    def __init__(self):
        self.name = "NOVA"

    def respond(self, text):
        text = text.strip()

        if not text:
            return "Please tell me what you need."

        lower = text.lower()

        # Greetings
        greetings = (
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
        )

        if lower in greetings:
            return "Hello! I am NOVA. How can I help you today?"

        # Identity
        if "who are you" in lower:
            return (
                "I am NOVA, your AI assistant. "
                "I can help with learning, questions, "
                "memory, daily content and other tasks."
            )

        # Name
        if lower in ("what is your name", "your name"):
            return "My name is NOVA."

        # Time
        if lower in ("time", "what time is it", "current time"):
            return datetime.now().strftime(
                "The current time is %H:%M."
            )

        # Date
        if lower in (
            "date",
            "what is today's date",
            "what is the date",
            "today",
        ):
            return datetime.now().strftime(
                "Today is %A, %d %B %Y."
            )

        # Simple conversation
        if lower in ("how are you", "how are you doing"):
            return "I'm working well and ready to help."

        if lower in ("thank you", "thanks"):
            return "You're welcome!"

        if lower in ("bye", "goodbye", "exit", "quit"):
            return "Goodbye! NOVA will be here when you need me."

        # Calculator
        result = self.calculate(text)

        if result is not None:
            return f"The answer is {result}"

        # Definitions
        if lower.startswith("what is "):
            return self.explain(text[8:].strip())

        if lower.startswith("define "):
            return self.explain(text[7:].strip())

        if lower.startswith("explain "):
            return self.explain(text[8:].strip())

        if lower.startswith("meaning of "):
            return self.explain(text[11:].strip())

        return (
            "I don't have an answer for that yet. "
            "I can help with calculations, definitions, "
            "basic conversation and learning."
        )

    def calculate(self, text):
        expression = text.lower()

        expression = expression.replace("what is", "")
        expression = expression.replace("calculate", "")
        expression = expression.replace("compute", "")
        expression = expression.strip()

        if not re.fullmatch(
            r"[0-9+\-*/().%\s]+",
            expression,
        ):
            return None

        if not any(
            operator in expression
            for operator in "+-*/%"
        ):
            return None

        try:
            result = eval(
                expression,
                {"__builtins__": {}},
                {},
            )

            if isinstance(result, float):
                if result.is_integer():
                    return int(result)

                return round(result, 6)

            return result

        except Exception:
            return None

    def explain(self, subject):

        definitions = {
            "computer":
                "A computer is an electronic device that "
                "processes data according to instructions.",

            "algorithm":
                "An algorithm is a step-by-step procedure "
                "for solving a problem.",

            "python":
                "Python is a high-level programming language "
                "used for software development, automation "
                "and many other tasks.",

            "programming":
                "Programming is the process of writing "
                "instructions that computers can execute.",

            "mathematics":
                "Mathematics is the study of numbers, "
                "quantities, patterns, structures and logic.",

            "biology":
                "Biology is the study of living organisms.",

            "chemistry":
                "Chemistry is the study of matter, its "
                "properties and the changes it undergoes.",

            "physics":
                "Physics studies matter, energy, motion, "
                "forces and their interactions.",

            "geography":
                "Geography studies places, people, "
                "environments and their relationships.",

            "history":
                "History is the study of past events "
                "and their effects on societies.",

            "entrepreneurship":
                "Entrepreneurship involves identifying "
                "opportunities and organizing resources "
                "to create value.",
        }

        key = subject.lower()

        if key in definitions:
            return definitions[key]

        return (
            f"I don't have a built-in definition for "
            f"'{subject}' yet."
        )


brain = NovaBrain()


def ask_brain(text):
    return brain.respond(text)


def respond(text):
    return brain.respond(text)
