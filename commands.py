from brain import ask_brain
from ai import ask_ai
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
    log_event,
    get_history,
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

        log_event(
            "lesson",
            f"Taught {subject} {form} {topic.replace('_', ' ')}"
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



    # ---------------- AI / BRAIN ----------------

    ai_result = ask_ai(command)

    if ai_result:
        return ai_result

    return ask_brain(command)
