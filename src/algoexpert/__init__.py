import importlib
import asyncio
import os
import logging
from typing import Optional, List, Any
from dotenv import load_dotenv

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

class AlgoExpert:
    def __init__(
        self,
        exchange: str,
        instrument: str,
        timeframes: List[str] = ['1m'],
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        base_url: str = "",
        contract: str = "",
        mode: str = "",
    ):
        logger.info(f"Initializing AlgoExpert for exchange: {exchange}, instrument: {instrument}")
        load_dotenv()  # Load .env file from the current working directory
        self.timeframes = timeframes

        try:
            logger.debug(f"Loading adapter for exchange: {exchange}")
            module = importlib.import_module(f".exchanges.{exchange}", package="algoexpert")
            adapter_class = getattr(module, f"{exchange.capitalize()}Adapter")
            logger.info(f"Successfully found adapter for {exchange}")
        except (ImportError, AttributeError) as e:
            logger.error(f"Failed to load adapter for exchange: {exchange}", exc_info=True)
            raise ValueError(f"Unsupported exchange: {exchange}") from e

        # Load credentials from environment if not provided
        api_key = api_key or os.getenv(f"{exchange.upper()}_API_KEY")
        api_secret = api_secret or os.getenv(f"{exchange.upper()}_API_SECRET")

        if not api_key or not api_secret:
            logger.error("API key and secret are required but not found.")
            raise ValueError(
                f"API key and secret for {exchange.upper()} are required. "
                f"Provide them to the constructor or set them as environment variables "
                f"(e.g., {exchange.upper()}_API_KEY)."
            )

        self.adapter = adapter_class(
            api_key=api_key,
            api_secret=api_secret,
            base_url=base_url,
            instrument=instrument,
            contract=contract,
            mode=mode,
        )
        logger.info(f"Successfully initialized adapter for {exchange}")

    def balance(self):
        return self.adapter.balance()

    def on_init(self, *args, **kwargs):
        return self.adapter.on_init(*args, **kwargs)

    def on_deinit(self, *args, **kwargs):
        return self.adapter.on_deinit(*args, **kwargs)

    def on_tick(self, *args, **kwargs):
        return self.adapter.on_tick(*args, **kwargs)

    def on_bar(self, bar: Any, timeframe: str):
        return self.adapter.on_bar(bar, timeframe)

    def on_timer(self, *args, **kwargs):
        return self.adapter.on_timer(*args, **kwargs)

    def on_trade(self, *args, **kwargs):
        return self.adapter.on_trade(*args, **kwargs)

    def on_transaction(self, *args, **kwargs):
        return self.adapter.on_transaction(*args, **kwargs)

    def on_book(self, *args, **kwargs):
        return self.adapter.on_book(*args, **kwargs)

    async def run(self):
        logger.info("Starting expert advisor run loop...")
        await self.adapter.run()
        logger.info("Expert advisor run loop finished.")
