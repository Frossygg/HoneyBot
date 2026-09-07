from app.trades.manager import TradeManager


def test_watching_ticker_can_be_created():
    manager = TradeManager()

    play = manager.create_play(
        admin_id=1001,
        ticker="NVDA",
        state="WATCHING",
    )

    assert play.ticker == "NVDA"
    assert play.state == "WATCHING"
    assert play.contract_complete is False


def test_full_contract_can_be_active():
    manager = TradeManager()

    play = manager.create_play(
        admin_id=1001,
        ticker="TSLA",
        state="ACTIVE",
        strike="387.5",
        option_type="CALL",
        expiration="9/11",
    )

    assert play.state == "ACTIVE"
    assert play.contract_complete is True


def test_in_on_different_ticker_does_not_change_watched_ticker():
    manager = TradeManager()

    nvda = manager.create_play(
        admin_id=1001,
        ticker="NVDA",
        state="WATCHING",
    )

    tsla = manager.apply_explicit_play(
        admin_id=1001,
        ticker="TSLA",
        state="ACTIVE",
        strike="387.5",
        option_type="CALL",
        expiration="9/11",
    )

    assert nvda.state == "WATCHING"

    assert tsla.ticker == "TSLA"
    assert tsla.state == "ACTIVE"
    assert tsla.strike == "387.5"


def test_in_on_same_ticker_updates_existing_watch():
    manager = TradeManager()

    manager.create_play(
        admin_id=1001,
        ticker="NVDA",
        state="WATCHING",
    )

    nvda = manager.apply_explicit_play(
        admin_id=1001,
        ticker="NVDA",
        state="ACTIVE",
        strike="230",
        option_type="CALL",
        expiration="9/11",
    )

    assert nvda.state == "ACTIVE"
    assert nvda.ticker == "NVDA"
    assert nvda.strike == "230"
    assert nvda.option_type == "CALL"
    assert nvda.expiration == "9/11"