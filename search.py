def search(query):
    query = query.strip()

    if not query:
        return "Please provide something to search for."

    return f"Search requested: {query}"
