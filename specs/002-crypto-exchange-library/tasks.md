# Tasks: Crypto Exchange Library

## Phase 3.1: Setup

- [x] T001: Project structure is already created.
- [x] T002: Dependencies are already listed in `pyproject.toml`.
- [x] T003: Linting and formatting tools (ruff) are already configured in `pyproject.toml`.

## Phase 3.2: Tests First (TDD)

- [ ] T004 [P]: Create a contract test for the `ExchangeAdapter` protocol in `tests/contract/test_exchange_adapter.py`. This test should check that the `BinanceAdapter` and `BybitAdapter` classes implement the protocol.
- [ ] T005 [P]: Create an integration test for Binance connection in `tests/integration/test_binance_connection.py`. This test should try to connect to the Binance API using dummy credentials and assert that it gets an authentication error.
- [ ] T006 [P]: Create an integration test for Bybit connection in `tests/integration/test_bybit_connection.py`. This test should do the same as the Binance test.

## Phase 3.3: Core Implementation

- [ ] T007: Implement the `BinanceAdapter` class in `src/algoexpert/exchanges/binance.py`. This class should implement the `ExchangeAdapter` protocol. For now, it can have placeholder methods.
- [ ] T008: Implement the `BybitAdapter` class in `src/algoexpert/exchanges/bybit.py`. This class should also implement the `ExchangeAdapter` protocol with placeholder methods.
- [ ] T009: Implement the main `AlgoExpert` class in `src/algoexpert/__init__.py`. This class will replace the protocol. It should dynamically load the correct adapter (Binance or Bybit) based on the `exchange` parameter in its `__init__` method.

## Phase 3.4: Integration

- [ ] T010: Implement the `connect` method in `BinanceAdapter` to actually connect to the Binance API.
- [ ] T011: Implement the `connect` method in `BybitAdapter` to actually connect to the Bybit API.

## Phase 3.5: Polish

- [ ] T012 [P]: Add unit tests for the `AlgoExpert` class logic in `tests/unit/test_algo_expert.py`.
- [ ] T013 [P]: Update `README.md` with the new architecture and usage examples.
- [ ] T014 [P]: Update the `docs` directory with more detailed documentation.
