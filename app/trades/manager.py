from app.trades.models import TradePlay


class TradeManager:
    def __init__(self):
        self.plays = {}

    def get_admin_plays(self, admin_id):
        return self.plays.get(admin_id, [])

    def create_play(
        self,
        admin_id,
        ticker,
        state,
        strike=None,
        option_type=None,
        expiration=None,
    ):
        play = TradePlay(
            admin_id=admin_id,
            ticker=ticker,
            state=state,
            strike=strike,
            option_type=option_type,
            expiration=expiration,
        )

        if admin_id not in self.plays:
            self.plays[admin_id] = []

        self.plays[admin_id].append(play)

        return play

    def find_open_plays_by_ticker(self, admin_id, ticker):
        admin_plays = self.get_admin_plays(admin_id)

        matches = []

        for play in admin_plays:
            if play.ticker == ticker and play.state != "CLOSED":
                matches.append(play)

        return matches

    def apply_explicit_play(
        self,
        admin_id,
        ticker,
        state,
        strike=None,
        option_type=None,
        expiration=None,
    ):
        matches = self.find_open_plays_by_ticker(admin_id, ticker)

        # No existing play for this ticker:
        # create a brand-new one.
        if len(matches) == 0:
            return self.create_play(
                admin_id=admin_id,
                ticker=ticker,
                state=state,
                strike=strike,
                option_type=option_type,
                expiration=expiration,
            )

        # More than one matching play is ambiguous.
        if len(matches) > 1:
            return None

        # Exactly one matching play:
        # update that existing play.
        play = matches[0]

        play.state = state

        if strike is not None:
            play.strike = strike

        if option_type is not None:
            play.option_type = option_type

        if expiration is not None:
            play.expiration = expiration

        return play