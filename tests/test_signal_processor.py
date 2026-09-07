from app.signal_parser import parse_signal
from app.signal_processor import SignalProcessor


def test_watch_creates_watching_play():
    processor = SignalProcessor()

    signal = parse_signal("Watching NVDA")

    play = processor.process(
        admin_id=1001,
        signal=signal,
    )

    assert play.ticker == "NVDA"
    assert play.state == "WATCHING"
    assert play.contract_complete is False


def test_in_different_ticker_creates_separate_play():
    processor = SignalProcessor()

    watch_signal = parse_signal("Watching NVDA")

    nvda = processor.process(
        admin_id=1001,
        signal=watch_signal,
    )

    in_signal = parse_signal("In TSLA 387.5C 9/11")

    tsla = processor.process(
        admin_id=1001,
        signal=in_signal,
    )

    assert nvda.ticker == "NVDA"
    assert nvda.state == "WATCHING"

    assert tsla.ticker == "TSLA"
    assert tsla.state == "ACTIVE"
    assert tsla.strike == "387.5"


def test_in_same_ticker_updates_existing_watch():
    processor = SignalProcessor()

    processor.process(
        admin_id=1001,
        signal=parse_signal("Watching NVDA"),
    )

    nvda = processor.process(
        admin_id=1001,
        signal=parse_signal("In NVDA 230C 9/11"),
    )

    assert nvda.ticker == "NVDA"
    assert nvda.state == "ACTIVE"
    assert nvda.strike == "230"
    assert nvda.option_type == "CALL"
    assert nvda.expiration == "9/11"