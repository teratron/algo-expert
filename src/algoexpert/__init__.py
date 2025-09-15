import importlib

class AlgoExpert:
    def __init__(self, exchange: str, api_key: str, api_secret: str, base_url: str, instrument: str, contract: str, mode: str):
        try:
            module = importlib.import_module(f".exchanges.{exchange}", package="algoexpert")
            adapter_class = getattr(module, f"{exchange.capitalize()}Adapter")
            self.adapter = adapter_class(
                api_key=api_key,
                api_secret=api_secret,
                base_url=base_url,
                instrument=instrument,
                contract=contract,
                mode=mode
            )
        except (ImportError, AttributeError):
            raise ValueError(f"Unsupported exchange: {exchange}")

    def balance(self):
        return self.adapter.balance()

    def on_init(self, *args, **kwargs):
        return self.adapter.on_init(*args, **kwargs)

    def on_deinit(self, *args, **kwargs):
        return self.adapter.on_deinit(*args, **kwargs)

    def on_tick(self, *args, **kwargs):
        return self.adapter.on_tick(*args, **kwargs)

    def on_bar(self, *args, **kwargs):
        return self.adapter.on_bar(*args, **kwargs)

    def on_timer(self, *args, **kwargs):
        return self.adapter.on_timer(*args, **kwargs)

    def on_trade(self, *args, **kwargs):
        return self.adapter.on_trade(*args, **kwargs)

    def on_transaction(self, *args, **kwargs):
        return self.adapter.on_transaction(*args, **kwargs)

    def on_book(self, *args, **kwargs):
        return self.adapter.on_book(*args, **kwargs)

    def run(self):
        return self.adapter.run()