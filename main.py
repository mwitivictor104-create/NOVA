from ai import NovaAI
from voice import speak, listen, voice_status, stop_speaking


def main():
    nova = NovaAI()

    print("================================")
    print("        NOVA AI ASSISTANT")
    print("================================")
    print("Hello Boss Victor.")
    print("Type 'voice' for voice mode.")
    print("Type 'exit' to quit.")

    speak("Hello Boss Victor. NOVA is ready.")

    while True:
        try:
            command = input("\nYou: ").strip()

            if not command:
                continue

            if command.lower() in ["exit", "quit"]:
                stop_speaking()
                speak("Goodbye Boss Victor.")
                print("NOVA: Goodbye Boss Victor.")
                break

            if command.lower() == "voice":
                voice_mode(nova)
                continue

            response = nova.respond(command)

            if response:
                print("NOVA:", response)
                speak(response)

        except KeyboardInterrupt:
            stop_speaking()
            print("\nNOVA stopped.")
            break

        except Exception as e:
            print("NOVA error:", e)


def voice_mode(nova):
    print("\n================================")
    print("          NOVA VOICE MODE")
    print("================================")
    print("Say 'Hi Nova' to begin.")
    print("Say 'exit' or 'quit' to leave voice mode.")

    speak("Yes Boss Victor, I am listening.")

    while True:
        try:
            text = listen()

            if not text:
                continue

            text = text.strip()
            print("You:", text)

            lower = text.lower()

            if lower in ["exit", "quit", "goodbye nova"]:
                stop_speaking()
                speak("Goodbye Boss Victor.")
                print("Leaving voice mode.")
                break

            if lower in [
                "stop",
                "stop speaking",
                "nova stop",
                "be quiet",
                "be quiet nova",
                "quiet"
            ]:
                stop_speaking()
                continue

            response = nova.respond(text)

            if response:
                print("NOVA:", response)
                speak(response)

        except KeyboardInterrupt:
            stop_speaking()
            print("\nLeaving voice mode.")
            break

        except Exception as e:
            print("Voice error:", e)


if __name__ == "__main__":
    main()
