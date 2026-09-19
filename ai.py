import os
import json
import urllib.request
import urllib.error


API_URL = os.environ.get(
    "NOVA_AI_URL",
    ""
)

API_KEY = os.environ.get(
    "OPENAI_API_KEY",
    ""
)

MODEL = os.environ.get(
    "NOVA_AI_MODEL",
    "gpt-5.6"
)


def ai_available():
    return bool(API_URL and API_KEY)


def ask_ai(prompt):
    if not ai_available():
        return None

    payload = {
        "model": MODEL,
        "input": prompt,
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(
            request,
            timeout=30,
        ) as response:

            raw = response.read().decode("utf-8")
            result = json.loads(raw)

            return extract_response(result)

    except (
        urllib.error.URLError,
        urllib.error.HTTPError,
        TimeoutError,
        json.JSONDecodeError,
        Exception,
    ):
        return None


def extract_response(data):
    if not isinstance(data, dict):
        return None

    # Common Responses API structure
    output_text = data.get("output_text")

    if output_text:
        return output_text.strip()

    # Try output blocks
    output = data.get("output")

    if isinstance(output, list):
        texts = []

        for item in output:
            if not isinstance(item, dict):
                continue

            content = item.get("content", [])

            if not isinstance(content, list):
                continue

            for block in content:
                if not isinstance(block, dict):
                    continue

                text = block.get("text")

                if text:
                    texts.append(str(text))

        if texts:
            return "\n".join(texts).strip()

    # Compatibility with older chat-style APIs
    choices = data.get("choices")

    if isinstance(choices, list) and choices:
        message = choices[0].get("message", {})

        if isinstance(message, dict):
            content = message.get("content")

            if content:
                return str(content).strip()

    return None
