def parse_signal(message_text):
    text = message_text.strip()

    if text.lower().startswith("load "):
        return {
            "action": "LOAD",
            "raw_message": text,
        }

    return None