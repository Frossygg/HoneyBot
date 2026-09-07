from app.parsing.action_parser import detect_action
from app.parsing.contract_parser import extract_contract


def parse_signal(message_text):
    action = detect_action(message_text)
    contract = extract_contract(message_text)

    if action is None:
        return None

    if contract is None:
        return None

    return {
        "action": action,
        "ticker": contract["ticker"],
        "strike": contract["strike"],
        "option_type": contract["option_type"],
        "expiration": contract["expiration"],
        "raw_message": message_text.strip(),
    }