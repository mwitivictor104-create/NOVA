from command_router import route


class NovaChatbot:

    def __init__(self):
        self.name = "NOVA"

    def respond(self, text):
        return route(text)

    def chat(self, text):
        return route(text)


chatbot = NovaChatbot()


def chat(text):
    return chatbot.respond(text)


def respond(text):
    return chatbot.respond(text)


if __name__ == "__main__":

    print("================================")
    print("       NOVA CHAT")
    print("================================")
    print("Type 'exit' to quit.")

    while True:

        try:
            text = input("\nYou: ").strip()

        except (EOFError, KeyboardInterrupt):
            print("\nNOVA: Goodbye!")
            break

        if not text:
            continue

        if text.lower() in (
            "exit",
            "quit",
            "goodbye",
        ):
            print("NOVA: Goodbye!")
            break

        print("NOVA:", respond(text))
