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
