import re


def detect_action(message_text):
    text = message_text.strip()

    normalized_text = text.replace("’", "'")

    # Explicitly reject phrases telling HoneyBot NOT to load.
    negated_load_patterns = [
        r"\bdon't\s+load\b",
        r"\bdont\s+load\b",
        r"\bdo\s+not\s+load\b",
    ]

    for pattern in negated_load_patterns:
        if re.search(pattern, normalized_text, re.IGNORECASE):
            return None

    # Detect WATCH / WATCHING.
    watch_pattern = r"\bwatch(?:ing)?\b"

    if re.search(watch_pattern, normalized_text, re.IGNORECASE):
        return "WATCH"

    # Detect LOAD / LOADING / LOADED.
    load_pattern = r"\bload(?:ing|ed)?\b"

    if re.search(load_pattern, normalized_text, re.IGNORECASE):
        return "LOAD"

    return None