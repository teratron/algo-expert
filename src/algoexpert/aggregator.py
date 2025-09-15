import logging
import re
from datetime import datetime, timedelta
from typing import Callable, Dict, List

logger = logging.getLogger(__name__)


def parse_timeframe(tf_str: str) -> timedelta:
    """Parses a timeframe string like '1s', '1m', '5m', '1h', '1d' into a timedelta object."""
    match = re.match(r"(\d+)([smhd])", tf_str.lower())
    if not match:
        raise ValueError(f"Invalid timeframe string: {tf_str}")

    value, unit = int(match.group(1)), match.group(2)
    if unit == 's':
        return timedelta(seconds=value)
    if unit == 'm':
        return timedelta(minutes=value)
    if unit == 'h':
        return timedelta(hours=value)
    if unit == 'd':
        return timedelta(days=value)
    raise ValueError(f"Unsupported timeframe unit: {unit}")  # Should not be reached


class Bar:
    """Represents a single OHLCV bar."""

    def __init__(self, open_price: float, timestamp: datetime, timeframe: timedelta):
        self.open = open_price
        self.high = open_price
        self.low = open_price
        self.close = open_price
        self.volume = 0.0
        self.timeframe = timeframe
        # Calculate the floored start time for the bar
        self.start_time = timestamp - (timestamp - datetime.min) % timeframe

    def add_trade(self, price: float, quantity: float):
        """Update the bar with a new trade."""
        self.high = max(self.high, price)
        self.low = min(self.low, price)
        self.close = price
        self.volume += quantity

    def __repr__(self):
        return (
            f"Bar(O={self.open}, H={self.high}, L={self.low}, C={self.close}, "
            f"V={self.volume}, T='{self.start_time}')"
        )


class BarAggregator:
    """Aggregates ticks into bars for multiple timeframes."""

    def __init__(self, timeframes: List[str], on_bar_callback: Callable[['Bar', str], None]):
        self.timeframes = {tf_str: parse_timeframe(tf_str) for tf_str in timeframes}
        self.on_bar = on_bar_callback
        self.current_bars: Dict[str, 'Bar'] = {}

    def add_tick(self, price: float, quantity: float, timestamp_ms: int):
        """
        Processes a new tick and updates the current bars or creates new ones.
        """
        tick_time = datetime.fromtimestamp(timestamp_ms / 1000.0)

        for tf_str, tf_delta in self.timeframes.items():
            current_bar = self.current_bars.get(tf_str)

            # Check if the tick belongs to the current bar
            if current_bar and tick_time < current_bar.start_time + tf_delta:
                # Tick belongs to the current bar, just update it
                current_bar.add_trade(price, quantity)
            else:
                # Tick belongs to a new bar.
                if current_bar:
                    # The old bar is complete, trigger the callback
                    logger.info(f"New {tf_str} bar completed: {current_bar}")
                    self.on_bar(current_bar, tf_str)

                # Start a new bar and add the first trade
                new_bar = Bar(price, tick_time, tf_delta)
                new_bar.add_trade(price, quantity)
                self.current_bars[tf_str] = new_bar
