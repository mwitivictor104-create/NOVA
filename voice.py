import shutil
import subprocess
import threading
import os

TTS_PROCESS = None
TTS_LOCK = threading.Lock()


def command_exists(command):
    return shutil.which(command) is not None


def voice_status():
    return {
        "tts": command_exists("termux-tts-speak"),
        "speech_to_text": command_exists("termux-speech-to-text"),
        "media_player": command_exists("termux-media-player")
    }


def stop_speaking():
    global TTS_PROCESS

    with TTS_LOCK:
        try:
            subprocess.run(
                ["termux-tts-speak", "--stop"],
                timeout=3,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        except Exception:
            pass

        try:
            if TTS_PROCESS and TTS_PROCESS.poll() is None:
                TTS_PROCESS.terminate()
        except Exception:
            pass

        TTS_PROCESS = None

    return True


def speak(text):
    global TTS_PROCESS

    if not text or not command_exists("termux-tts-speak"):
        return False

    stop_speaking()

    try:
        TTS_PROCESS = subprocess.Popen(
            ["termux-tts-speak", str(text)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return True

    except Exception:
        TTS_PROCESS = None
        return False


def play_listening_beep():
    beep = os.path.expanduser(
        "~/NOVA/sounds/listening_beep.wav"
    )

    if not os.path.exists(beep):
        return False

    if not command_exists("termux-media-player"):
        return False

    try:
        subprocess.run(
            ["termux-media-player", "play", beep],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=3
        )
        return True
    except Exception:
        return False


def listen():
    if not command_exists("termux-speech-to-text"):
        return ""

    play_listening_beep()

    try:
        result = subprocess.run(
            ["termux-speech-to-text"],
            capture_output=True,
            text=True,
            timeout=60
        )

        return result.stdout.strip()

    except Exception:
        return ""


def status():
    info = voice_status()

    print("NOVA VOICE STATUS")
    print("=================")

    print(
        "Text-to-speech:",
        "OK" if info["tts"] else "NOT AVAILABLE"
    )

    print(
        "Speech-to-text:",
        "OK" if info["speech_to_text"] else "NOT AVAILABLE"
    )

    print(
        "Media player:",
        "OK" if info["media_player"] else "NOT AVAILABLE"
    )


if __name__ == "__main__":
    status()
