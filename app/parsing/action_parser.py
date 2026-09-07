import re


def detect_action(message_text):
    text = message_text.strip()

    load_pattern = r"\bload(?:ing|ed)?\b"

    if re.search(load_pattern, text, re.IGNORECASE):
        return "LOAD"

    return None