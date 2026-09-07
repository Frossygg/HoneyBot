import re


def extract_ticker(message_text):
    text = message_text.strip()

    pattern = r"\b(?:watch|watching)\s+([A-Za-z]{1,6})\b"

    match = re.search(pattern, text, re.IGNORECASE)

    if not match:
        return None

    return match.group(1).upper()