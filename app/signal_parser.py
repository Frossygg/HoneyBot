import re


def parse_signal(message_text):
    text = message_text.strip()

    pattern = r"load\s+([A-Za-z]+)\s+(\d+(?:\.\d+)?)([CP])\s+(\d{1,2}/\d{1,2})"

    match = re.search(pattern, text, re.IGNORECASE)

    if not match:
        return None

    ticker = match.group(1).upper()
    strike = match.group(2)
    option_letter = match.group(3).upper()
    expiration = match.group(4)

    option_type = "CALL" if option_letter == "C" else "PUT"

    return {
        "action": "LOAD",
        "ticker": ticker,
        "strike": strike,
        "option_type": option_type,
        "expiration": expiration,
        "raw_message": text,
    }