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

def test_dont_load_is_not_a_load_signal():
    result = parse_signal("Don't load NVDA 230C 9/11 yet")

    assert result is None   

def test_watching_only_needs_ticker():
    result = parse_signal("Watching NVDA")

    assert result is not None
    assert result["action"] == "WATCH"
    assert result["ticker"] == "NVDA"
    assert result["strike"] is None
    assert result["option_type"] is None
    assert result["expiration"] is None 

def test_watching_full_contract_is_allowed():
    result = parse_signal("Watching NVDA 230C 9/11")

    assert result is not None
    assert result["action"] == "WATCH"
    assert result["ticker"] == "NVDA"
    assert result["strike"] == "230"
    assert result["option_type"] == "CALL"
    assert result["expiration"] == "9/11"

def test_in_with_full_contract_is_parsed():
    result = parse_signal("In TSLA 387.5C 9/11")

    assert result is not None
    assert result["action"] == "IN"
    assert result["ticker"] == "TSLA"
    assert result["strike"] == "387.5"
    assert result["option_type"] == "CALL"
    assert result["expiration"] == "9/11"


def test_bare_in_does_not_guess_yet():
    result = parse_signal("In")

    assert result is None
    