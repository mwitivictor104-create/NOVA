import time
from ai import NovaAI

def main():
    nova = NovaAI()

    print("NOVA background service started for Boss Victor.")

    while True:
        try:
            # Keep NOVA alive in the background.
            # Background features can be added here later.
            time.sleep(60)

        except KeyboardInterrupt:
            print("NOVA background service stopped.")
            break

        except Exception as e:
            print("NOVA background error:", e)
            time.sleep(10)

if __name__ == "__main__":
    main()
