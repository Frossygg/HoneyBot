from dataclasses import dataclass


@dataclass
class TradePlay:
    admin_id: int
    ticker: str
    state: str

    strike: str | None = None
    option_type: str | None = None
    expiration: str | None = None

    @property
    def contract_complete(self):
        return (
            self.strike is not None
            and self.option_type is not None
            and self.expiration is not None
        )