from app.signal_parser import parse_signal


def test_standard_load_call():
    result = parse_signal("Load NVDA 230C 9/11")

    assert result is not None
    assert result["action"] == "LOAD"
    assert result["ticker"] == "NVDA"
    assert result["strike"] == "230"
    assert result["option_type"] == "CALL"
    assert result["expiration"] == "9/11"


def test_loading_is_recognized():
    result = parse_signal("Loading NVDA 230C 9/11")

    assert result is not None
    assert result["action"] == "LOAD"


def test_load_at_end_is_recognized():
    result = parse_signal("NVDA 230C 9/11 load")

    assert result is not None
    assert result["action"] == "LOAD"


def test_space_between_strike_and_call():
    result = parse_signal("Load NVDA 230 C 9/11")

    assert result is not None
    assert result["ticker"] == "NVDA"
    assert result["option_type"] == "CALL"


def test_call_word_is_supported():
    result = parse_signal("Load NVDA 230 CALL 9/11")

    assert result is not None
    assert result["option_type"] == "CALL"


def test_decimal_strike():
    result = parse_signal("Load TSLA 387.5C 9/4")

    assert result is not None
    assert result["strike"] == "387.5"


def test_put_is_supported():
    result = parse_signal("Load SPY 680P 9/11")

    assert result is not None
    assert result["option_type"] == "PUT"


def test_normal_message_is_ignored():
    result = parse_signal("Good morning everyone")

    assert result is None