"""AlgoExpert trading bot implementation using EMA (Exponential Moving Average) strategy"""
import os
import pandas as pd
from dotenv import load_dotenv

from algoexpert import AlgoExpert

# Load environment variables from .env file
load_dotenv()

# Initialize AlgoExpert with Bybit connection parameters
expert = AlgoExpert(
    exchange="bybit",
    api_key=os.getenv("BYBIT_API_KEY"),
    api_secret=os.getenv("BYBIT_API_SECRET"),
    base_url=os.getenv("BYBIT_BASE_URL"),
    market_type="futures",   # Using futures market
    contract_type="coin_m",  # Coin-margined contracts
    mode="paper",            # Paper trading mode (no real trades)
)

# Check account balance before starting
expert.balance()


@expert.on_init(
    symbol="BTCUSDT", interval="1h", shift=0,
    strategy_id=12345, name="EMA Expert",
    quantity=0.01, stop_loss=100, take_profit=200,
    trailing_stop=50, slippage=10, max_positions=5
)
def init() -> None:
    """Initialization function called once when the expert advisor starts."""
    print("*** on_init ***")


@expert.on_deinit
def deinit(reason) -> None:
    """Deinitialization function called when the expert advisor stops."""
    print("*** on_deinit ***", reason)


@expert.on_tick
def tick(rates) -> None:
    """Called on each tick (price update) from the market."""
    print("*** on_tick ***", rates)


@expert.on_bar("1h")
def bar(rates) -> None:
    """Called when a new 1-hour bar is formed."""
    print(f"*** on_bar received {len(rates)} rates ***")

    try:
        df = pd.DataFrame([{'close': r.close} for r in rates])

        if len(df) < 8:
            print("Not enough data to calculate EMA crossover. Skipping.")
            return

        fast_ema_period = 3
        slow_ema_period = 7
        df['fast_ema'] = df['close'].ewm(span=fast_ema_period, adjust=False).mean()
        df['slow_ema'] = df['close'].ewm(span=slow_ema_period, adjust=False).mean()

        last_row = df.iloc[-1]
        prev_row = df.iloc[-2]

        if prev_row['fast_ema'] < prev_row['slow_ema'] and last_row['fast_ema'] > last_row['slow_ema']:
            print("BUY SIGNAL DETECTED: Fast EMA crossed above Slow EMA.")
            expert.buy()
            print("Executing BUY trade.")

        elif prev_row['fast_ema'] > prev_row['slow_ema'] and last_row['fast_ema'] < last_row['slow_ema']:
            print("SELL SIGNAL DETECTED: Fast EMA crossed below Slow EMA.")
            expert.sell()
            print("Executing SELL trade.")

    except Exception as e:
        print(f"An error occurred in on_bar: {e}")


@expert.on_timer(1)
def timer() -> None:
    """Called every 1 second to perform time-based operations."""
    print("*** on_timer 1 sec. ***")


@expert.on_timer(3)
def timer2() -> None:
    """Called every 3 seconds to perform time-based operations."""
    print("*** on_timer 3 sec. ***")


@expert.on_trade
def trade() -> None:
    """Called when a trade operation is performed."""
    print("*** on_trade ***")


@expert.on_transaction
def transaction(request, result) -> None:
    """Called when a transaction is completed."""
    print("*** on_transaction ***", request, result)


@expert.on_book("BTCUSDT")
def book() -> None:
    """Called when the order book for BTCUSDT is updated."""
    print("*** on_book ***")


def main() -> None:
    """Main entry point for the EMA expert advisor."""
    expert.run()


if __name__ == "__main__":
    main()