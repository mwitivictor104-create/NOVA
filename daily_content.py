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
