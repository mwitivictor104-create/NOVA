def get_weather(location=""):
    if location:
        return f"Weather service ready for {location}."
    return "Weather service ready."
