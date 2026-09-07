from app.signal_parser import parse_signal


def test_load_signal_is_detected():
    result = parse_signal("Load NVDA 230C 9/11")

    assert result is not None
    assert result["action"] == "LOAD"


def test_normal_message_is_ignored():
    result = parse_signal("Good morning everyone")

    assert result is None