"""
NOVA Knowledge Base
Simple built-in definitions and explanations.
"""

KNOWLEDGE = {
    "python": (
        "Python is a high-level programming language known for "
        "readable syntax and broad use in automation, data science, "
        "web development, and artificial intelligence."
    ),

    "ai": (
        "Artificial intelligence is the field of creating computer "
        "systems that can perform tasks that normally require human "
        "intelligence, such as learning, reasoning, and understanding language."
    ),

    "computer": (
        "A computer is an electronic device that processes data "
        "according to instructions called programs."
    ),

    "algorithm": (
        "An algorithm is a step-by-step procedure used to solve a "
        "problem or complete a task."
    ),

    "database": (
        "A database is an organized collection of information that "
        "can be stored, searched, and managed electronically."
    ),

    "network": (
        "A computer network is a group of connected devices that "
        "communicate and share information or resources."
    ),

    "html": (
        "HTML stands for HyperText Markup Language. It is used to "
        "structure content on web pages."
    ),

    "css": (
        "CSS stands for Cascading Style Sheets. It controls the "
        "appearance and layout of web pages."
    ),

    "javascript": (
        "JavaScript is a programming language commonly used to make "
        "web pages interactive and dynamic."
    ),

    "business": (
        "Business is the activity of producing, buying, selling, or "
        "providing goods and services to satisfy people's needs and wants."
    ),

    "mathematics": (
        "Mathematics is the study of numbers, quantities, structures, "
        "patterns, shapes, and logical relationships."
    ),

    "physics": (
        "Physics is the study of matter, energy, motion, forces, and "
        "the interactions between them."
    ),

    "chemistry": (
        "Chemistry is the study of matter, its properties, composition, "
        "structure, and the changes it undergoes."
    ),

    "biology": (
        "Biology is the scientific study of living organisms and life processes."
    ),

    "geography": (
        "Geography is the study of places, people, environments, and "
        "the relationships between humans and the physical world."
    ),
}


def normalize(term):
    """Normalize a knowledge query."""
    return str(term).strip().lower()


def define(term):
    """
    Return a definition from NOVA's knowledge base.

    Returns None when the term is not found.
    """
    key = normalize(term)

    if key in KNOWLEDGE:
        return KNOWLEDGE[key]

    return None


def search_knowledge(query):
    """
    Search the built-in knowledge base.

    Returns matching terms and definitions.
    """
    query = normalize(query)

    if not query:
        return []

    results = []

    for term, definition in KNOWLEDGE.items():
        if query in term or query in definition.lower():
            results.append({
                "term": term,
                "definition": definition,
            })

    return results


def list_topics():
    """Return all available knowledge topics."""
    return sorted(KNOWLEDGE.keys())
