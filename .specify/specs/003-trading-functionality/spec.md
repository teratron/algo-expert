# Feature Specification: Trading Functionality

**Feature Branch**: `003-trading-functionality`
**Status**: Draft

## Description

This feature will implement the core trading loop of the `AlgoExpert` library. This includes connecting to the exchange's websocket, listening for market data, and triggering the corresponding event handlers (`on_tick`, `on_bar`, etc.).

## Requirements

### Technical Requirements

- **TR-001**: The `run` method in the `ExchangeAdapter` protocol shall be implemented in both `BinanceAdapter` and `BybitAdapter`.
- **TR-002**: The `run` method shall establish a websocket connection to the exchange's market data stream.
- **TR-003**: The websocket connection shall be maintained, with automatic reconnection in case of disconnection.
- **TR-004**: Incoming websocket messages shall be parsed and mapped to the appropriate event handlers:
    - `on_tick` for new trades.
    - `on_book` for order book updates.
- **TR-005**: The implementation shall use the `websockets` library, which is already a dependency.
- **TR-006**: The implementation shall be asynchronous, using `asyncio`.

## Proposal

I propose we start by implementing the `run` method in the `BinanceAdapter`. We will focus on connecting to the Binance websocket and handling tick data (new trades). Once this is working, we can move on to the `BybitAdapter` and then add more event handlers.

What do you think about this proposal?
