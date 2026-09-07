import re


def extract_contract(message_text):
    text = message_text.strip()

    pattern = (
        r"\b([A-Za-z]{1,6})\s+"
        r"(\d+(?:\.\d+)?)\s*"
        r"(CALL|PUT|C|P)\s+"
        r"(\d{1,2}/\d{1,2})\b"
    )

    match = re.search(pattern, text, re.IGNORECASE)

    if not match:
        return None

    ticker = match.group(1).upper()
    strike = match.group(2)
    option_text = match.group(3).upper()
    expiration = match.group(4)

    if option_text in ("C", "CALL"):
        option_type = "CALL"
    else:
        option_type = "PUT"

    return {
        "ticker": ticker,
        "strike": strike,
        "option_type": option_type,
        "expiration": expiration,
    }