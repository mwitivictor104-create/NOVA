#!/usr/bin/env python3

import os
import json
import random

BASE = os.path.dirname(os.path.abspath(__file__))
LESSONS = os.path.join(BASE, "lessons")
DATA = os.path.join(BASE, "data")

os.makedirs(LESSONS, exist_ok=True)
os.makedirs(DATA, exist_ok=True)


# ============================================================
# SUBJECT DATABASE
# ============================================================

subjects_py = r'''
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LESSONS_DIR = os.path.join(BASE_DIR, "lessons")

DEFAULT_SUBJECTS = [
    "mathematics",
    "english",
    "kiswahili",
    "biology",
    "chemistry",
    "physics",
    "geography",
    "history",
    "cre",
    "business",
    "agriculture",
    "computer",
]


def normalize(text):
    return (
        str(text)
        .strip()
        .lower()
        .replace("-", "_")
        .replace(" ", "_")
    )


def discover_subjects():
    result = {
        subject: {}
        for subject in DEFAULT_SUBJECTS
    }

    if not os.path.isdir(LESSONS_DIR):
        return result

    for subject in os.listdir(LESSONS_DIR):

        subject_path = os.path.join(
            LESSONS_DIR,
            subject
        )

        if not os.path.isdir(subject_path):
            continue

        subject = normalize(subject)

        if subject not in result:
            result[subject] = {}

        for form in os.listdir(subject_path):

            form_path = os.path.join(
                subject_path,
                form
            )

            if not os.path.isdir(form_path):
                continue

            form = normalize(form)

            result[subject].setdefault(
                form,
                []
            )

            for filename in os.listdir(form_path):

                if not filename.lower().endswith(".txt"):
                    continue

                topic = normalize(
                    filename[:-4]
                )

                if topic not in result[subject][form]:
                    result[subject][form].append(
                        topic
                    )

    for subject in result:
        for form in result[subject]:
            result[subject][form].sort()

    return result


SUBJECTS = discover_subjects()


def refresh_subjects():
    global SUBJECTS
    SUBJECTS = discover_subjects()
    return SUBJECTS


def available_subjects():
    refresh_subjects()
    return list(SUBJECTS.keys())


def available_forms(subject):
    refresh_subjects()
    return list(
        SUBJECTS.get(
            normalize(subject),
            {}
        ).keys()
    )


def available_topics(subject, form):
    refresh_subjects()

    return SUBJECTS.get(
        normalize(subject),
        {}
    ).get(
        normalize(form),
        []
    )


# Compatibility with older NOVA code.
def list_subjects():
    return available_subjects()


def list_topics(subject, form=None):

    refresh_subjects()

    subject = normalize(subject)

    if form:
        return available_topics(
            subject,
            form
        )

    result = []

    for current_form, topics in SUBJECTS.get(
        subject,
        {}
    ).items():

        for topic in topics:
            result.append(
                f"{current_form}: {topic}"
            )

    return result


if __name__ == "__main__":

    print("NOVA SUBJECT DATABASE")
    print("=====================")
    print()

    for subject, forms in SUBJECTS.items():

        print(subject.upper())

        for form, topics in forms.items():

            print(f"  {form}")

            for topic in topics:
                print(
                    "    - "
                    + topic.replace(
                        "_",
                        " "
                    ).title()
                )

        print()
'''


# ============================================================
# LESSON ENGINE
# ============================================================

lesson_engine_py = r'''
import os

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


def normalize(text):
    return (
        str(text)
        .strip()
        .lower()
        .replace("-", "_")
        .replace(" ", "_")
    )


def find_lesson(
    subject,
    form,
    topic
):

    subject = normalize(subject)
    form = normalize(form)
    topic = normalize(topic)

    path = os.path.join(
        BASE_DIR,
        "lessons",
        subject,
        form,
        topic + ".txt"
    )

    if not os.path.isfile(path):
        return None

    try:
        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:
            return file.read().strip()

    except Exception as error:
        return (
            "Could not read lesson: "
            + str(error)
        )


def teach(
    subject,
    form,
    topic
):

    lesson = find_lesson(
        subject,
        form,
        topic
    )

    if lesson is None:

        path = (
            f"lessons/"
            f"{normalize(subject)}/"
            f"{normalize(form)}/"
            f"{normalize(topic)}.txt"
        )

        return (
            "Lesson not found: "
            + path
        )

    return lesson
'''


# ============================================================
# MEMORY
# ============================================================

memory_py = r'''
import os
import json

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

MEMORY_FILE = os.path.join(
    BASE_DIR,
    "data",
    "memory.json"
)


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    try:

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return data if isinstance(
            data,
            dict
        ) else {}

    except Exception:
        return {}


def save_memory(memory):

    os.makedirs(
        os.path.dirname(MEMORY_FILE),
        exist_ok=True
    )

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            memory,
            file,
            indent=2,
            ensure_ascii=False
        )


def remember(key, value):

    key = str(key).strip()
    value = str(value).strip()

    if not key:
        return False

    memory = load_memory()
    memory[key] = value

    save_memory(memory)

    return True


def recall(key):

    return load_memory().get(
        str(key).strip()
    )


def forget(key):

    key = str(key).strip()

    memory = load_memory()

    if key not in memory:
        return False

    del memory[key]

    save_memory(memory)

    return True


def all_memory():
    return load_memory()
'''


# ============================================================
# DAILY CONTENT
# ============================================================

daily_content_py = r'''
import random


DEVOTIONS = [
    {
        "title": "Wisdom",
        "message": "Learning and patience help us grow stronger each day.",
        "verse": "Proverbs 4:7"
    },
    {
        "title": "Courage",
        "message": "Face today's challenges with courage and patience.",
        "verse": "Joshua 1:9"
    },
    {
        "title": "Hope",
        "message": "A difficult day does not decide your entire future.",
        "verse": "Romans 15:13"
    },
    {
        "title": "Patience",
        "message": "Progress often takes time, practice and consistency.",
        "verse": "Romans 12:12"
    },
    {
        "title": "Faith",
        "message": "Keep doing what is right even when results take time.",
        "verse": "Hebrews 11:1"
    },
]


MOTIVATIONS = [
    "Keep learning. Keep practicing. Keep improving.",
    "Small consistent steps can produce big results.",
    "Your mistakes can become lessons when you learn from them.",
    "Practice turns knowledge into skill.",
    "Progress is built one step at a time.",
    "Do not give up simply because something is difficult.",
]


def daily_content(command="devotion"):

    command = str(command).lower()

    if "motivat" in command:

        return random.choice(
            MOTIVATIONS
        )

    item = random.choice(
        DEVOTIONS
    )

    return (
        f"{item['title']}\n\n"
        f"{item['message']}\n\n"
        f"Bible reference: "
        f"{item['verse']}"
    )
'''


# ============================================================
# LEARNING ENGINE
# ============================================================

learning_py = r'''
import os
import json

from subjects import (
    SUBJECTS,
    refresh_subjects,
    available_subjects,
    available_forms,
    available_topics,
)

from lesson_engine import find_lesson


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

PROGRESS_FILE = os.path.join(
    BASE_DIR,
    "data",
    "progress.json"
)


def normalize(text):

    return (
        str(text)
        .strip()
        .lower()
        .replace("-", "_")
        .replace(" ", "_")
    )


def get_lesson(
    subject,
    form,
    topic
):

    return find_lesson(
        normalize(subject),
        normalize(form),
        normalize(topic)
    )


def lesson_exists(
    subject,
    form,
    topic
):

    return get_lesson(
        subject,
        form,
        topic
    ) is not None


def search_lessons(keyword):

    refresh_subjects()

    keyword = normalize(keyword)
    results = []

    for subject, forms in SUBJECTS.items():

        for form, topics in forms.items():

            for topic in topics:

                combined = (
                    f"{subject} "
                    f"{form} "
                    f"{topic}"
                )

                if keyword in normalize(
                    combined
                ):

                    results.append(
                        combined
                    )

    return results


def lesson_summary(
    subject,
    form,
    topic
):

    lesson = get_lesson(
        subject,
        form,
        topic
    )

    if lesson is None:
        return None

    lines = [
        line.strip()
        for line in lesson.splitlines()
        if line.strip()
    ]

    return "\n".join(
        lines[:15]
    )


def extract_section(
    lesson,
    names
):

    lines = lesson.splitlines()

    active = False
    result = []

    names = {
        str(name).upper()
        for name in names
    }

    for line in lines:

        clean = line.strip()
        upper = clean.upper()

        if upper in names:
            active = True
            continue

        if active:

            if upper in (
                "SUMMARY",
                "KEY POINTS",
                "ANSWERS",
                "ANSWER KEY",
                "PRACTICE",
                "PRACTICE QUESTIONS",
                "EXERCISES"
            ):
                break

            if clean:
                result.append(clean)

    return result


def practice(
    subject,
    form,
    topic
):

    lesson = get_lesson(
        subject,
        form,
        topic
    )

    if lesson is None:
        return (
            f"Lesson not found: "
            f"{subject}/{form}/{topic}"
        )

    questions = extract_section(
        lesson,
        [
            "PRACTICE",
            "PRACTICE QUESTIONS",
            "EXERCISES"
        ]
    )

    if not questions:
        return (
            "This lesson does not yet "
            "have practice questions."
        )

    return "\n".join(
        questions
    )


def load_progress():

    if not os.path.exists(
        PROGRESS_FILE
    ):
        return {}

    try:

        with open(
            PROGRESS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return data if isinstance(
            data,
            dict
        ) else {}

    except Exception:
        return {}


def save_progress(data):

    os.makedirs(
        os.path.dirname(
            PROGRESS_FILE
        ),
        exist_ok=True
    )

    with open(
        PROGRESS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=2
        )


def mark_completed(
    subject,
    form,
    topic
):

    progress = load_progress()

    key = (
        f"{normalize(subject)}:"
        f"{normalize(form)}:"
        f"{normalize(topic)}"
    )

    progress.setdefault(
        key,
        {
            "subject": normalize(subject),
            "form": normalize(form),
            "topic": normalize(topic),
            "completed": False,
            "attempts": 0,
            "best_score": 0,
            "last_score": 0
        }
    )

    progress[key]["completed"] = True

    save_progress(progress)


def continue_learning():

    refresh_subjects()

    progress = load_progress()

    for subject, forms in SUBJECTS.items():

        for form, topics in forms.items():

            for topic in topics:

                key = (
                    f"{subject}:"
                    f"{form}:"
                    f"{topic}"
                )

                if not progress.get(
                    key,
                    {}
                ).get(
                    "completed",
                    False
                ):

                    return {
                        "subject": subject,
                        "form": form,
                        "topic": topic
                    }

    return None


def progress_report():

    progress = load_progress()

    if not progress:

        return (
            "NOVA LEARNING PROGRESS\n\n"
            "No progress recorded yet."
        )

    output = [
        "NOVA LEARNING PROGRESS",
        ""
    ]

    for record in progress.values():

        output.append(
            f"{record['subject'].title()} "
            f"{record['form']} "
            f"{record['topic'].replace('_', ' ').title()}"
        )

        output.append(
            "  Completed: "
            + str(
                record.get(
                    "completed",
                    False
                )
            )
        )

        output.append("")

    return "\n".join(output)


def curriculum():

    refresh_subjects()

    output = []

    for subject, forms in SUBJECTS.items():

        output.append(
            subject.upper()
        )

        for form, topics in forms.items():

            output.append(
                f"  {form}"
            )

            for topic in topics:

                output.append(
                    "    - "
                    + topic.replace(
                        "_",
                        " "
                    ).title()
                )

        output.append("")

    return "\n".join(output)
'''


# ============================================================
# VOICE
# ============================================================

voice_py = r'''
import shutil
import subprocess


def command_exists(command):
    return shutil.which(command) is not None


def voice_status():

    return {
        "tts": command_exists(
            "termux-tts-speak"
        ),

        "speech_to_text": command_exists(
            "termux-speech-to-text"
        )
    }


def speak(text):

    if not text:
        return False

    if not command_exists(
        "termux-tts-speak"
    ):
        return False

    try:

        subprocess.run(
            [
                "termux-tts-speak",
                str(text)
            ],
            timeout=30
        )

        return True

    except Exception:
        return False


def listen():

    if not command_exists(
        "termux-speech-to-text"
    ):
        return ""

    try:

        result = subprocess.run(
            [
                "termux-speech-to-text"
            ],
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
        "OK" if info["tts"]
        else "NOT AVAILABLE"
    )

    print(
        "Speech-to-text:",
        "OK" if info["speech_to_text"]
        else "NOT AVAILABLE"
    )


if __name__ == "__main__":
    status()
'''


# ============================================================
# COMMAND ENGINE
# ============================================================

commands_py = r'''
from subjects import (
    available_subjects,
    available_forms,
    available_topics,
)

from lesson_engine import teach

from learning import (
    practice,
    lesson_summary,
    search_lessons,
    curriculum,
    mark_completed,
    continue_learning,
    progress_report,
)

from daily_content import daily_content

from memory import (
    remember,
    recall,
    forget,
    all_memory,
)


def teach_command(text):

    parts = text.split()

    if len(parts) < 3:
        return (
            "Use: teach "
            "<subject> <form> <topic>"
        )

    subject = parts[0]
    form = parts[1]
    topic = " ".join(parts[2:])

    result = teach(
        subject,
        form,
        topic
    )

    if not result.startswith(
        "Lesson not found:"
    ):

        mark_completed(
            subject,
            form,
            topic
        )

    return result


def execute(command):

    if not command:
        return ""

    command = command.strip()
    lower = command.lower()


    if lower in (
        "exit",
        "quit"
    ):
        return "Goodbye."


    if lower in (
        "hello",
        "hi",
        "hey",
        "hello nova",
        "hi nova"
    ):

        return (
            "Hello! I am NOVA. "
            "How can I help you?"
        )


    if lower in (
        "help",
        "commands"
    ):

        return """NOVA COMMANDS

GENERAL
  hello
  help
  status

LEARNING
  subjects
  forms <subject>
  topics <subject> <form>
  teach <subject> <form> <topic>
  practice <subject> <form> <topic>
  summary <subject> <form> <topic>
  search lesson <keyword>
  curriculum
  continue learning
  progress

DAILY
  devotion
  motivation

MEMORY
  remember <key> = <value>
  recall <key>
  forget <key>
  memory
"""


    if lower == "status":

        return """NOVA STATUS

Core: OK
Learning: OK
Memory: OK
Daily content: OK
"""


    if lower in (
        "subjects",
        "subject"
    ):

        return (
            "AVAILABLE SUBJECTS\n\n"
            + "\n".join(
                "- " + subject.title()
                for subject in available_subjects()
            )
        )


    if lower.startswith(
        "forms "
    ):

        subject = command[6:].strip()

        forms = available_forms(
            subject
        )

        if not forms:
            return (
                f"No forms found for "
                f"{subject}."
            )

        return (
            f"FORMS — {subject.title()}\n\n"
            + "\n".join(
                "- " + form
                for form in forms
            )
        )


    if lower.startswith(
        "topics "
    ):

        parts = command.split()

        if len(parts) < 3:
            return (
                "Use: topics "
                "<subject> <form>"
            )

        subject = parts[1]
        form = parts[2]

        topics = available_topics(
            subject,
            form
        )

        if not topics:
            return (
                f"No topics found for "
                f"{subject} {form}."
            )

        return (
            f"TOPICS — "
            f"{subject.title()} {form}\n\n"
            + "\n".join(
                "- "
                + topic.replace(
                    "_",
                    " "
                ).title()
                for topic in topics
            )
        )


    if lower.startswith(
        "teach "
    ):

        return teach_command(
            command[6:].strip()
        )


    if lower.startswith(
        "practice "
    ):

        parts = command.split()

        if len(parts) < 4:
            return (
                "Use: practice "
                "<subject> <form> <topic>"
            )

        return practice(
            parts[1],
            parts[2],
            " ".join(parts[3:])
        )


    if lower.startswith(
        "summary "
    ):

        parts = command.split()

        if len(parts) < 4:
            return (
                "Use: summary "
                "<subject> <form> <topic>"
            )

        result = lesson_summary(
            parts[1],
            parts[2],
            " ".join(parts[3:])
        )

        return result or "Lesson not found."


    if lower.startswith(
        "search lesson "
    ):

        keyword = command[
            len("search lesson "):
        ].strip()

        if not keyword:
            return (
                "Use: search lesson <keyword>"
            )

        results = search_lessons(
            keyword
        )

        if not results:
            return (
                f"No lessons found for: "
                f"{keyword}"
            )

        return (
            "LESSON SEARCH RESULTS\n\n"
            + "\n".join(
                "- " + result
                for result in results
            )
        )


    if lower == "curriculum":
        return curriculum()


    if lower in (
        "continue",
        "continue learning",
        "resume learning"
    ):

        result = continue_learning()

        if result is None:
            return (
                "All registered lessons "
                "have been completed."
            )

        return (
            "NEXT LESSON\n\n"
            f"Subject: "
            f"{result['subject'].title()}\n"
            f"Form: {result['form']}\n"
            f"Topic: "
            f"{result['topic'].replace('_', ' ').title()}\n\n"
            f"Use: teach "
            f"{result['subject']} "
            f"{result['form']} "
            f"{result['topic']}"
        )


    if lower in (
        "progress",
        "learning progress",
        "my progress"
    ):

        return progress_report()


    if lower in (
        "devotion",
        "daily devotion",
        "daily"
    ):

        return daily_content(
            "devotion"
        )


    if lower in (
        "motivation",
        "motivate",
        "daily motivation"
    ):

        return daily_content(
            "motivation"
        )


    if lower.startswith(
        "remember "
    ):

        data = command[9:].strip()

        if "=" not in data:
            return (
                "Use: remember "
                "<key> = <value>"
            )

        key, value = data.split(
            "=",
            1
        )

        if remember(
            key.strip(),
            value.strip()
        ):

            return (
                "Memory saved: "
                + key.strip()
            )

        return "Could not save memory."


    if lower.startswith(
        "recall "
    ):

        key = command[7:].strip()

        value = recall(key)

        if value is None:
            return (
                "No memory found for: "
                + key
            )

        return (
            f"{key}: {value}"
        )


    if lower.startswith(
        "forget "
    ):

        key = command[7:].strip()

        if forget(key):
            return (
                "Forgot: " + key
            )

        return (
            "No memory found for: "
            + key
        )


    if lower in (
        "memory",
        "memories",
        "show memory"
    ):

        data = all_memory()

        if not data:
            return (
                "NOVA memory is empty."
            )

        return "\n".join(
            [
                "NOVA MEMORY",
                ""
            ]
            + [
                f"- {key}: {value}"
                for key, value in data.items()
            ]
        )


    return (
        "I do not recognize that command.\n\n"
        "Type 'help' to see available commands."
    )
'''


# ============================================================
# MAIN
# ============================================================

main_py = r'''
#!/usr/bin/env python3

from commands import execute
from voice import (
    speak,
    listen,
    voice_status
)


def text_mode():

    print()
    print("=== NOVA TEXT MODE ===")
    print("Type 'exit' to return.")
    print()

    while True:

        try:

            user_input = input(
                "You: "
            ).strip()

            if not user_input:
                continue

            if user_input.lower() in (
                "exit",
                "quit"
            ):
                break

            response = execute(
                user_input
            )

            print()
            print("NOVA:")
            print(response)
            print()

        except KeyboardInterrupt:
            break

        except Exception as error:

            print(
                "NOVA ERROR:",
                error
            )


def voice_mode():

    status = voice_status()

    if not status["speech_to_text"]:

        print()
        print(
            "Speech-to-text is not available."
        )
        print()

        return

    print()
    print("=== NOVA VOICE MODE ===")
    print("Say 'exit' to return.")
    print()

    speak(
        "NOVA voice mode is ready."
    )

    while True:

        print("Listening...")

        text = listen()

        if not text:
            print(
                "NOVA: I did not hear anything."
            )
            continue

        print(
            "You:",
            text
        )

        if text.lower() in (
            "exit",
            "quit",
            "stop"
        ):

            speak(
                "Returning to the main menu."
            )

            break

        try:

            response = execute(
                text
            )

            print()
            print("NOVA:")
            print(response)
            print()

            if status["tts"]:
                speak(response)

        except Exception as error:

            print(
                "NOVA ERROR:",
                error
            )


def show_status():

    status = voice_status()

    print()
    print("=== NOVA STATUS ===")
    print()
    print("Core: OK")
    print("Text mode: OK")
    print(
        "Text-to-speech:",
        "OK" if status["tts"]
        else "NOT AVAILABLE"
    )
    print(
        "Speech-to-text:",
        "OK" if status["speech_to_text"]
        else "NOT AVAILABLE"
    )
    print()


def main():

    print()
    print("================================")
    print("       NOVA AI ASSISTANT")
    print("================================")
    print()

    while True:

        print("Choose a mode:")
        print("1. Text")
        print("2. Voice")
        print("3. Status")
        print("4. Exit")
        print()

        try:

            choice = input(
                "NOVA > "
            ).strip().lower()

        except KeyboardInterrupt:

            print(
                "\nNOVA: Goodbye."
            )

            break

        if choice in (
            "1",
            "text"
        ):

            text_mode()

        elif choice in (
            "2",
            "voice"
        ):

            voice_mode()

        elif choice in (
            "3",
            "status"
        ):

            show_status()

        elif choice in (
            "4",
            "exit",
            "quit"
        ):

            print(
                "NOVA: Goodbye."
            )

            break

        else:

            print(
                "NOVA: Please choose "
                "1, 2, 3 or 4."
            )

        print()


if __name__ == "__main__":
    main()
'''


FILES = {
    "subjects.py": subjects_py,
    "lesson_engine.py": lesson_engine_py,
    "memory.py": memory_py,
    "daily_content.py": daily_content_py,
    "learning.py": learning_py,
    "voice.py": voice_py,
    "commands.py": commands_py,
    "main.py": main_py,
}


for filename, content in FILES.items():

    path = os.path.join(
        BASE,
        filename
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            content.strip()
            + "\n"
        )

    print(
        "RESTORED:",
        filename
    )


# ============================================================
# INITIAL DATA FILES
# ============================================================

memory_file = os.path.join(
    DATA,
    "memory.json"
)

if not os.path.exists(
    memory_file
):

    with open(
        memory_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            {},
            file,
            indent=2
        )


progress_file = os.path.join(
    DATA,
    "progress.json"
)

if not os.path.exists(
    progress_file
):

    with open(
        progress_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            {},
            file,
            indent=2
        )


print()
print("==============================")
print("NOVA CORE RESTORATION COMPLETE")
print("==============================")
print()
print("Existing lessons were preserved.")
print("Existing data was preserved.")
print()
