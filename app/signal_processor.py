from app.trades.manager import TradeManager


class SignalProcessor:
    def __init__(self):
        self.trade_manager = TradeManager()

    def process(self, admin_id, signal):
        action = signal["action"]

        state_map = {
            "WATCH": "WATCHING",
            "LOAD": "LOADED",
            "IN": "ACTIVE",
        }

        state = state_map.get(action)

        if state is None:
            return None

        return self.trade_manager.apply_explicit_play(
            admin_id=admin_id,
            ticker=signal["ticker"],
            state=state,
            strike=signal["strike"],
            option_type=signal["option_type"],
            expiration=signal["expiration"],
        )