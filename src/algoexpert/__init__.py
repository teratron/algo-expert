from typing import Protocol, runtime_checkable

# Here we will import the exchange modules
from .exchanges import binance, bybit


@runtime_checkable
class AlgoExpert(Protocol):
    def __init__(self, stock: str, api_key: str, api_secret: str, base_url: str, instrument: str, contract: str, mode: str):
        # Here we will dynamically select the exchange
        ...

    def balance(self):
        ...

    def on_init(self, *args, **kwargs):
        ...

    def on_deinit(self, *args, **kwargs):
        ...

    def on_tick(self, *args, **kwargs):
        ...

    def on_bar(self, *args, **kwargs):
        ...

    def on_timer(self, *args, **kwargs):
        ...

    def on_trade(self, *args, **kwargs):
        ...

    def on_transaction(self, *args, **kwargs):
        ...

    def on_book(self, *args, **kwargs):
        ...

    def run(self):
        ...
