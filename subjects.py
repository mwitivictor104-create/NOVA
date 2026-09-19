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
