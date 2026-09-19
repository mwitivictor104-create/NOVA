import re

from brain import respond as brain_respond
from lesson_engine import teach
import learning


def _parse_teach(command):
    """
    Parse:
        teach mathematics form 1 numbers
        teach biology form 1 cell
        teach physics form 3 motion
    """

    pattern = r"^\s*teach\s+(.+?)\s+(form\s*\d+)\s+(.+?)\s*$"
    match = re.match(pattern, command, re.IGNORECASE)

    if not match:
        return None

    subject = match.group(1).strip()
    form = match.group(2).strip().replace(" ", "")
    topic = match.group(3).strip()

    return subject, form, topic


def _parse_practice(command):
    """
    Parse:
        practice mathematics form 1 numbers
    """

    pattern = r"^\s*practice\s+(.+?)\s+(form\s*\d+)\s+(.+?)\s*$"
    match = re.match(pattern, command, re.IGNORECASE)

    if not match:
        return None

    subject = match.group(1).strip()
    form = match.group(2).strip().replace(" ", "")
    topic = match.group(3).strip()

    return subject, form, topic


def route(command):
    if not command:
        return "Please tell me what you need."

    command = command.strip()

    lower = command.lower()

    # ---------------------------------------------------------
    # TEACH
    # ---------------------------------------------------------

    parsed = _parse_teach(command)

    if parsed:
        subject, form, topic = parsed

        lesson = teach(
            subject,
            form,
            topic
        )

        if lesson and not lesson.startswith("Lesson not found:"):
            try:
                learning.mark_lesson_started(
                    subject,
                    form,
                    topic
                )
            except Exception:
                pass

        return lesson

    # ---------------------------------------------------------
    # PRACTICE
    # ---------------------------------------------------------

    parsed = _parse_practice(command)

    if parsed:
        subject, form, topic = parsed

        try:
            result = learning.practice(
                subject,
                form,
                topic
            )

            if result:
                return str(result)

        except TypeError:
            pass

        except Exception as error:
            return f"Practice error: {error}"

        lesson = learning.get_lesson(
            subject,
            form,
            topic
        )

        if not lesson:
            return (
                f"Lesson not found: "
                f"{subject} {form} {topic}"
            )

        practice = learning.extract_practice(
            lesson
        )

        if practice:
            return practice

        return "No practice questions are available for this lesson yet."

    # ---------------------------------------------------------
    # PROGRESS
    # ---------------------------------------------------------

    if lower in (
        "progress",
        "my progress",
        "learning progress",
        "show progress",
    ):
        try:
            return str(learning.progress_report())
        except Exception as error:
            return f"Could not read progress: {error}"

    # ---------------------------------------------------------
    # SUBJECTS
    # ---------------------------------------------------------

    if lower in (
        "subjects",
        "list subjects",
        "available subjects",
    ):
        try:
            subjects = learning.available_subjects()

            if not subjects:
                return "No subjects are currently available."

            return (
                "Available subjects:\n\n"
                + "\n".join(
                    f"• {subject.title()}"
                    for subject in subjects
                )
            )

        except Exception as error:
            return f"Could not load subjects: {error}"

    # ---------------------------------------------------------
    # FALL BACK TO NOVA BRAIN
    # ---------------------------------------------------------

    try:
        return brain_respond(command)

    except Exception as error:
        return f"NOVA error: {error}"


def execute(command):
    return route(command)


if __name__ == "__main__":

    print("NOVA COMMAND ROUTER")
    print("===================")

    while True:

        try:
            command = input("\nYou: ").strip()

        except (EOFError, KeyboardInterrupt):
            print("\nNOVA: Goodbye!")
            break

        if command.lower() in (
            "exit",
            "quit",
            "goodbye",
        ):
            print("NOVA: Goodbye!")
            break

        print("NOVA:", route(command))
