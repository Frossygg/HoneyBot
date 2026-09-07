from app.parsing.action_parser import detect_action
from app.parsing.contract_parser import extract_contract
from app.parsing.ticker_parser import extract_ticker


def parse_signal(message_text):
    action = detect_action(message_text)

    if action is None:
        return None

    contract = extract_contract(message_text)

    # WATCH only requires a ticker.
    if action == "WATCH":
        # If the admin already gave us the full contract,
        # use all of that information.
        if contract is not None:
            return {
                "action": action,
                "ticker": contract["ticker"],
                "strike": contract["strike"],
                "option_type": contract["option_type"],
                "expiration": contract["expiration"],
                "raw_message": message_text.strip(),
            }

        # Otherwise, try to get just the ticker.
        ticker = extract_ticker(message_text)

        if ticker is None:
            return None

        return {
            "action": action,
            "ticker": ticker,
            "strike": None,
            "option_type": None,
            "expiration": None,
            "raw_message": message_text.strip(),
        }

    # LOAD still requires a complete contract for now.
    if action == "LOAD":
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
    if action == "IN":
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

    return None