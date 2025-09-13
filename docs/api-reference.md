# API Reference

This section provides a detailed reference for the classes and methods in the `algoexpert` library.

## The `AlgoExpert` Class

This is the main class of the library.

`AlgoExpert(exchange: str, api_key: str, api_secret: str, base_url: str, instrument: str, contract: str, mode: str)`

- `exchange`: The name of the exchange to connect to (e.g., "binance", "bybit").
- `api_key`: Your API key for the exchange.
- `api_secret`: Your API secret for the exchange.
- `base_url`: The base URL of the API. If not provided, the default for the exchange will be used.
- `instrument`: (Not yet implemented)
- `contract`: (Not yet implemented)
- `mode`: (Not yet implemented)

The `AlgoExpert` class provides the following methods, which correspond to the methods of the exchange adapter:

- `balance()`
- `on_init(*args, **kwargs)`
- `on_deinit(*args, **kwargs)`
- `on_tick(*args, **kwargs)`
- `on_bar(*args, **kwargs)`
- `on_timer(*args, **kwargs)`
- `on_trade(*args, **kwargs)`
- `on_transaction(*args, **kwargs)`
- `on_book(*args, **kwargs)`
- `run()`

## The `ExchangeAdapter` Protocol

This protocol defines the interface that all exchange adapters must implement.

- `__init__(self, api_key: str, api_secret: str, base_url: str, instrument: str, contract: str, mode: str)`
- `connect(self)`
- `balance(self)`
- `on_init(self, *args, **kwargs)`
- `on_deinit(self, *args, **kwargs)`
- `on_tick(self, *args, **kwargs)`
- `on_bar(self, *args, **kwargs)`
- `on_timer(self, *args, **kwargs)`
- `on_trade(self, *args, **kwargs)`
- `on_transaction(self, *args, **kwargs)`
- `on_book(self, *args, **kwargs)`
- `run(self)`
