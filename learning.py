import os
import json
import re

from subjects import available_subjects, available_forms, available_topics
from lesson_engine import find_lesson


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
PROGRESS_FILE = os.path.join(DATA_DIR, "progress.json")

os.makedirs(DATA_DIR, exist_ok=True)


def normalize(text):
    return re.sub(r"[^a-z0-9]+", "_", str(text).strip().lower()).strip("_")


# ============================================================
# LESSONS
# ============================================================

def get_lesson(subject, form, topic):
    return find_lesson(subject, form, topic)


def lesson_exists(subject, form, topic):
    return get_lesson(subject, form, topic) is not None


def search_lessons(keyword):
    keyword = normalize(keyword)
    results = []

    for subject in available_subjects():
        for form in available_forms(subject):
            for topic in available_topics(subject, form):
                if (
                    keyword in normalize(subject)
                    or keyword in normalize(form)
                    or keyword in normalize(topic)
                ):
                    results.append({
                        "subject": subject,
                        "form": form,
                        "topic": topic
                    })

    return results


def lesson_summary(subject, form, topic):
    lesson = get_lesson(subject, form, topic)

    if not lesson:
        return f"Lesson not found: {subject} {form} {topic}"

    lines = lesson.splitlines()

    title = ""
    objectives = []
    key_points = []

    section = ""

    for line in lines:
        text = line.strip()

        if not text:
            continue

        upper = text.upper()

        if upper == "TITLE":
            section = "title"
            continue

        if upper == "OBJECTIVES":
            section = "objectives"
            continue

        if upper == "KEY POINTS":
            section = "key_points"
            continue

        if upper in {
            "LESSON",
            "EXAMPLE",
            "PRACTICE",
            "ANSWERS"
        }:
            section = ""
            continue

        if section == "title" and not title:
            title = text

        elif section == "objectives":
            objectives.append(text)

        elif section == "key_points":
            key_points.append(text)

    output = []

    output.append(f"{subject.upper()} - {form.upper()} - {topic.upper()}")

    if title:
        output.append("")
        output.append(title)

    if objectives:
        output.append("")
        output.append("OBJECTIVES")
        output.extend(objectives[:5])

    if key_points:
        output.append("")
        output.append("KEY POINTS")
        output.extend(key_points[:8])

    if not objectives and not key_points:
        output.append("")
        output.append("Lesson is available.")

    return "\n".join(output)


# ============================================================
# SECTION PARSER
# ============================================================

MAJOR_SECTIONS = {
    "TITLE",
    "OBJECTIVES",
    "LESSON",
    "EXAMPLE",
    "KEY POINTS",
    "PRACTICE",
    "ANSWERS"
}


def _section_name(line):
    text = line.strip().upper()

    if text in MAJOR_SECTIONS:
        return text

    return None


def extract_section(text, section):
    if not text:
        return ""

    wanted = section.strip().upper()
    current = None
    result = []

    for line in text.splitlines():
        name = _section_name(line)

        if name:
            current = name
            continue

        if current == wanted:
            result.append(line.rstrip())

    return "\n".join(result).strip()


def extract_practice(text):
    return extract_section(text, "PRACTICE")


def extract_answers(text):
    return extract_section(text, "ANSWERS")


# ============================================================
# PROGRESS
# ============================================================

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return {}

    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data if isinstance(data, dict) else {}

    except Exception:
        return {}


def save_progress(data):
    os.makedirs(DATA_DIR, exist_ok=True)

    temp_file = PROGRESS_FILE + ".tmp"

    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    os.replace(temp_file, PROGRESS_FILE)


def progress_key(subject, form, topic):
    return f"{normalize(subject)}|{normalize(form)}|{normalize(topic)}"


def ensure_record(data, subject, form, topic):
    key = progress_key(subject, form, topic)

    if key not in data:
        data[key] = {
            "subject": subject,
            "form": form,
            "topic": topic,
            "started": False,
            "practice_started": False,
            "attempts": 0,
            "last_score": 0,
            "best_score": 0,
            "completed": False,
            "history": []
        }

    return data[key]


def mark_lesson_started(subject, form, topic):
    data = load_progress()

    record = ensure_record(data, subject, form, topic)
    record["started"] = True

    save_progress(data)
    return record


def mark_practice_started(subject, form, topic):
    data = load_progress()

    record = ensure_record(data, subject, form, topic)
    record["practice_started"] = True

    save_progress(data)
    return record


def save_quiz_result(subject, form, topic, score, total):
    data = load_progress()

    record = ensure_record(data, subject, form, topic)

    record["attempts"] += 1
    record["last_score"] = score
    record["best_score"] = max(record.get("best_score", 0), score)

    percentage = 0

    if total:
        percentage = round((score / total) * 100, 1)

    record["history"].append({
        "score": score,
        "total": total,
        "percentage": percentage
    })

    if percentage >= 70:
        record["completed"] = True

    save_progress(data)

    return record


def get_progress(subject=None, form=None, topic=None):
    data = load_progress()

    if subject and form and topic:
        return data.get(progress_key(subject, form, topic))

    return data


# ============================================================
# QUIZ
# ============================================================

def _clean_question(line):
    line = line.strip()

    if not line:
        return ""

    line = re.sub(r"^\s*(?:Q(?:UESTION)?\s*)?\d+\s*[\.\):-]\s*", "", line, flags=re.I)

    return line.strip()


def _clean_answer(line):
    line = line.strip()

    line = re.sub(
        r"^\s*(?:A(?:NSWER)?\s*)?\d+\s*[\.\):-]\s*",
        "",
        line,
        flags=re.I
    )

    line = re.sub(r"^\s*[-*•]\s*", "", line)

    return line.strip()


def _normalize_answer(answer):
    answer = str(answer).strip().lower()

    answer = re.sub(r"^[a-d][\.\):\-]\s*", "", answer)
    answer = re.sub(r"[^a-z0-9\s]", "", answer)
    answer = re.sub(r"\s+", " ", answer)

    return answer.strip()


def answers_match(user_answer, correct_answer):
    a = _normalize_answer(user_answer)
    b = _normalize_answer(correct_answer)

    if not a or not b:
        return False

    if a == b:
        return True

    # Allow a short answer to match a longer answer when the
    # normalized text is clearly equivalent.
    if len(a) >= 3 and (a in b or b in a):
        return True

    return False


def build_quiz(subject, form, topic):
    lesson = get_lesson(subject, form, topic)

    if not lesson:
        return []

    practice_text = extract_practice(lesson)
    answers_text = extract_answers(lesson)

    if not practice_text:
        return []

    questions = []

    for line in practice_text.splitlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith("#"):
            continue

        question = _clean_question(line)

        if question:
            questions.append(question)

    answers = []

    for line in answers_text.splitlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith("#"):
            continue

        answer = _clean_answer(line)

        if answer:
            answers.append(answer)

    quiz = []

    for index, question in enumerate(questions):
        answer = answers[index] if index < len(answers) else ""

        quiz.append({
            "question": question,
            "answer": answer
        })

    return quiz


def practice(subject, form, topic):
    lesson = get_lesson(subject, form, topic)

    if not lesson:
        return f"Lesson not found: {subject} {form} {topic}"

    mark_practice_started(subject, form, topic)

    practice_text = extract_practice(lesson)

    if not practice_text:
        return (
            f"No practice questions are available yet for "
            f"{subject} {form} {topic}."
        )

    return (
        f"PRACTICE: {subject.upper()} {form.upper()} - {topic.upper()}\n\n"
        + practice_text
    )


# ============================================================
# REPORTS
# ============================================================

def progress_report():
    data = load_progress()

    if not data:
        return "NOVA LEARNING PROGRESS\n\nNo progress recorded yet."

    total = len(data)
    completed = sum(
        1 for record in data.values()
        if record.get("completed")
    )

    started = sum(
        1 for record in data.values()
        if record.get("started")
    )

    lines = [
        "NOVA LEARNING PROGRESS",
        "",
        f"Lessons started: {started}",
        f"Lessons completed: {completed}",
        f"Topics tracked: {total}",
        ""
    ]

    for record in data.values():
        subject = record.get("subject", "")
        form = record.get("form", "")
        topic = record.get("topic", "")
        best = record.get("best_score", 0)
        attempts = record.get("attempts", 0)

        status = "COMPLETED" if record.get("completed") else "IN PROGRESS"

        lines.append(
            f"- {subject} {form} {topic}: "
            f"{status}, attempts={attempts}, best={best}"
        )

    return "\n".join(lines)


def continue_learning():
    data = load_progress()

    # First continue an unfinished tracked topic.
    for record in data.values():
        if not record.get("completed"):
            return {
                "subject": record.get("subject"),
                "form": record.get("form"),
                "topic": record.get("topic")
            }

    # Otherwise find the first available lesson.
    for subject in available_subjects():
        forms = available_forms(subject)

        for form in forms:
            topics = available_topics(subject, form)

            for topic in topics:
                return {
                    "subject": subject,
                    "form": form,
                    "topic": topic
                }

    return None


def study_plan():
    plan = []

    for subject in available_subjects():
        forms = available_forms(subject)

        for form in forms:
            topics = available_topics(subject, form)

            for topic in topics:
                plan.append({
                    "subject": subject,
                    "form": form,
                    "topic": topic
                })

    return plan


def weak_topics():
    data = load_progress()
    weak = []

    for record in data.values():
        best = record.get("best_score", 0)

        if record.get("attempts", 0) > 0 and best < 70:
            weak.append(record)

    return weak


def curriculum():
    result = []

    for subject in available_subjects():
        result.append(subject.upper())

        for form in available_forms(subject):
            topics = available_topics(subject, form)

            if topics:
                result.append(f"  {form}: " + ", ".join(topics))

    return "\n".join(result)


if __name__ == "__main__":
    print("NOVA learning module loaded successfully.")


# ============================================================
# COMPATIBILITY: MARK LESSON COMPLETED
# ============================================================

def mark_completed(subject, form, topic):
    data = load_progress()

    record = ensure_record(data, subject, form, topic)
    record["started"] = True
    record["completed"] = True

    save_progress(data)

    return record
