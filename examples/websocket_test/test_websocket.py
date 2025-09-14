import asyncio
import logging
from algoexpert import AlgoExpert

# --- CONFIGURATION ---
# Change this value to 'binance' or 'bybit' to test the respective exchange.
EXCHANGE_TO_TEST = "bybit"
INSTRUMENT = "BTCUSDT"
TIMEFRAMES = ['1m', '5m'] # The timeframes to aggregate bars for
# ---------------------

async def main():
    """
    Initializes and runs the AlgoExpert to test the websocket connection.
    
    This script relies on a .env file in the same directory.
    For Binance, it needs:
    BINANCE_API_KEY="YOUR_API_KEY"
    BINANCE_API_SECRET="YOUR_API_SECRET"

    For Bybit, it needs:
    BYBIT_API_KEY="YOUR_API_KEY"
    BYBIT_API_SECRET="YOUR_API_SECRET"
    """
    logger = logging.getLogger(__name__)
    
    logger.info(f"Initializing AlgoExpert for {EXCHANGE_TO_TEST}...")
    expert = AlgoExpert(
        exchange=EXCHANGE_TO_TEST,
        instrument=INSTRUMENT,
        timeframes=TIMEFRAMES
    )

    logger.info(f"Starting expert advisor to listen for trades on {INSTRUMENT} via {EXCHANGE_TO_TEST}...")
    await expert.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Expert advisor stopped manually.")
