"""AlgoExpert trading bot implementation using EMA (Exponential Moving Average) strategy"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
#import pandas as pd
from dotenv import load_dotenv

from algoexpert import AlgoExpert

# Load environment variables from .env file
load_dotenv()

# Initialize AlgoExpert with Binance connection parameters
expert = AlgoExpert(
    exchange="binance",
    instrument="BTCUSDT",
    api_key=os.getenv("BINANCE_API_KEY"),
    api_secret=os.getenv("BINANCE_API_SECRET"),
    base_url=os.getenv("BINANCE_BASE_URL"),
    market_type="futures",   # Using futures market
    contract_type="coin_m",  # Coin-margined contracts
    mode="paper",            # Paper trading mode (no real trades)
    log_file="binance_expert.log",
    trade_log_file="binance_trades.log",
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
    """Initialization function called once when the expert advisor starts.

    Sets up the trading parameters for BTCUSDT on 1-hour timeframe:
    - Trading lot size: 0.01
    - Stop loss: 100 points
    - Take profit: 200 points
    - Trailing stop: 50 points
    - Slippage: 10 points
    - Maximum positions: 5
    """
    print("*** on_init ***")


@expert.on_deinit
def deinit(reason) -> None:
    """Deinitialization function called when the expert advisor stops.

    Args:
        reason: The reason for deinitialization
    """
    print("*** on_deinit ***", reason)


@expert.on_tick
def tick(rates) -> None:
    """Called on each tick (price update) from the market.

    Args:
        rates: Current market rates information
    """
    print("*** on_tick ***", rates)


@expert.on_bar("1h")
def bar(rates) -> None:
    """Called when a new 1-hour bar is formed.
    This is where the main EMA trading logic is implemented.

    Args:
        rates: Bar data containing OHLCV information
    """
    print(f"*** on_bar received {len(rates)} rates ***")

    # --- EMA trading logic implementation ---
    # try:
    #     # 1. Create a DataFrame from the rates data
    #     # Assuming `rates` is a list of objects with a .close attribute
    #     df = pd.DataFrame([{'close': r.close} for r in rates])

    #     # We need at least 8 data points to compare a 7-period EMA with its previous value
    #     if len(df) < 8:
    #         print("Not enough data to calculate EMA crossover. Skipping.")
    #         return

    #     # 2. Calculate slow and fast EMAs
    #     fast_ema_period = 3
    #     slow_ema_period = 7
    #     df['fast_ema'] = df['close'].ewm(span=fast_ema_period, adjust=False).mean()
    #     df['slow_ema'] = df['close'].ewm(span=slow_ema_period, adjust=False).mean()

    #     # 3. Get the last two values to check for a crossover
    #     last_row = df.iloc[-1]
    #     prev_row = df.iloc[-2]

    #     # 4. Detect crossovers and generate signals
    #     # Golden Cross (Buy Signal)
    #     if prev_row['fast_ema'] < prev_row['slow_ema'] and last_row['fast_ema'] > last_row['slow_ema']:
    #         print("BUY SIGNAL DETECTED: Fast EMA crossed above Slow EMA.")
    #         # 5. Execute buy trade
    #         # Assuming expert.buy() is the method to open a long position
    #         # The quantity is taken from the @on_init decorator
    #         expert.buy()
    #         print("Executing BUY trade.")

    #     # Death Cross (Sell Signal)
    #     elif prev_row['fast_ema'] > prev_row['slow_ema'] and last_row['fast_ema'] < last_row['slow_ema']:
    #         print("SELL SIGNAL DETECTED: Fast EMA crossed below Slow EMA.")
    #         # 5. Execute sell trade
    #         # Assuming expert.sell() is the method to open a short position
    #         expert.sell()
    #         print("Executing SELL trade.")

    # except Exception as e:
    #     print(f"An error occurred in on_bar: {e}")


@expert.on_timer(1)
def timer() -> None:
    """Called every 1 second to perform time-based operations.
    Useful for operations that need to run periodically regardless of market activity.
    """
    print("*** on_timer 1 sec. ***")


@expert.on_timer(3)
def timer2() -> None:
    """Called every 3 seconds to perform time-based operations.
    Can be used for less frequent checks or updates.
    """
    print("*** on_timer 3 sec. ***")


@expert.on_trade
def trade() -> None:
    """Called when a trade operation is performed.
    Useful for tracking and managing open positions.
    """
    print("*** on_trade ***")


@expert.on_transaction
def transaction(request, result) -> None:
    """Called when a transaction is completed.

    Args:
        request: The transaction request details
        result: The result of the transaction
    """
    print("*** on_transaction ***", request, result)


@expert.on_book("BTCUSDT")
def book() -> None:
    """Called when the order book for BTCUSDT is updated.
    Can be used to implement order book analysis strategies.
    """
    print("*** on_book ***")


def main() -> None:
    """Main entry point for the EMA expert advisor.
    Starts the trading bot with the configured settings.
    """
    expert.run()


if __name__ == "__main__":
    main()
