class Engine:
    """
    NOVA Core Engine
    Controls the assistant lifecycle.
    """

    def __init__(self):
        self.running = False
        self.version = "2.0"

    def start(self):
        self.running = True
        print("NOVA Engine Started")

    def stop(self):
        self.running = False
        print("NOVA Engine Stopped")

    def restart(self):
        self.stop()
        self.start()

    def is_running(self):
        return self.running

    def get_version(self):
        return self.version
