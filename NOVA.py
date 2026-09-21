 ~/Nova/wake_nova.py

import subprocess
import os


NOVA_DIR = os.path.expanduser("~/NOVA")


def wake():

    try:

        subprocess.Popen(
            [
                "bash",
                "-c",
                f"cd {NOVA_DIR} && python main.py"
            ]
        )

        print("Nova awakened.")

    except Exception as e:

        print(
            "Wake error:",
            e
        )
