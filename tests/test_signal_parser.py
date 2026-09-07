from app.signal_parser import parse_signal


def test_load_call_signal_is_parsed():
    result = parse_signal("Load NVDA 230C 9/11")

    assert result is not None
    assert result["action"] == "LOAD"
    assert result["ticker"] == "NVDA"
    assert result["strike"] == "230"
    assert result["option_type"] == "CALL"
    assert result["expiration"] == "9/11"


def test_load_put_signal_is_parsed():
    result = parse_signal("Load SPY 680P 9/11")

    assert result is not None
    assert result["ticker"] == "SPY"
    assert result["strike"] == "680"
    assert result["option_type"] == "PUT"


def test_normal_message_is_ignored():
    result = parse_signal("Good morning everyone")

    assert result is None