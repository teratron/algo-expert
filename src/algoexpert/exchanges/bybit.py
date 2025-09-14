from pybit.unified_trading import HTTP
import asyncio
import websockets
import json
import logging
from typing import List
from ..aggregator import BarAggregator

logger = logging.getLogger(__name__)

class BybitAdapter:
    def __init__(
        self, 
        api_key: str, 
        api_secret: str, 
        base_url: str, 
        instrument: str, 
        contract: str, 
        mode: str,
        timeframes: List[str] = ['1m']
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url if base_url else "https://api.bybit.com"
        self.instrument = instrument
        # pybit's HTTP client uses the 'endpoint' parameter for the base URL
        self.client = HTTP(api_key=self.api_key, api_secret=self.api_secret, endpoint=self.base_url)
        
        # Initialize the bar aggregator for multiple timeframes
        self.aggregator = BarAggregator(timeframes=timeframes, on_bar_callback=self.on_bar)
        
        self.connect()

    def connect(self):
        """
        Tests the connection by making a call to the wallet balance endpoint.
        The client will raise an exception for non-2xx responses.
        """
        self.client.get_wallet_balance(accountType="UNIFIED")

    def balance(self):
        """
        Retrieves account balance information.
        The client will raise an exception for non-2xx responses.
        """
        return self.client.get_wallet_balance(accountType="UNIFIED")

    def on_init(self, *args, **kwargs):
        pass

    def on_deinit(self, *args, **kwargs):
        pass

    def on_tick(self, tick_payload: dict):
        """
        Processes a new tick payload from the trade stream and feeds it to the aggregator.
        Bybit sends a list of trades in the 'data' field.
        """
        try:
            for trade in tick_payload['data']:
                price = float(trade['p'])
                quantity = float(trade['v'])
                timestamp_ms = int(trade['T'])
                
                logger.debug(f"Processing tick: Price={price}, Qty={quantity}")
                self.aggregator.add_tick(price, quantity, timestamp_ms)
        except (KeyError, ValueError, TypeError) as e:
            logger.warning(f"Could not process tick data due to missing/invalid key or format: {e}. Data: {tick_payload}")

    def on_bar(self, bar, timeframe: str):
        """
        Called by the aggregator when a new bar is completed.
        """
        logger.info(f"New {timeframe} bar for {self.instrument}: {bar}")

    def on_timer(self, *args, **kwargs):
        pass

    def on_trade(self, *args, **kwargs):
        pass

    def on_transaction(self, *args, **kwargs):
        pass

    def on_book(self, *args, **kwargs):
        logger.info(f"New book update: {args}")

    async def run(self):
        uri = "wss://stream.bybit.com/v5/public/spot"
        trade_topic = f"publicTrade.{self.instrument}"
        book_topic = f"orderbook.50.{self.instrument}"
        
        subscription_message = {
            "op": "subscribe",
            "args": [trade_topic, book_topic]
        }

        while True:
            try:
                async with websockets.connect(uri) as websocket:
                    await websocket.send(json.dumps(subscription_message))
                    logger.info(f"Connected to Bybit websocket and subscribed to: {trade_topic}, {book_topic}")

                    while True:
                        message = await websocket.recv()
                        data = json.loads(message)
                        topic = data.get("topic")

                        if not topic:
                            logger.debug(f"Received non-topic message from Bybit: {data}")
                            continue

                        if topic == trade_topic:
                            self.on_tick(data)
                        elif topic == book_topic:
                            self.on_book(data)

            except Exception as e:
                logger.error(f"Bybit websocket connection failed: {e}. Reconnecting in 5 seconds...", exc_info=True)
                await asyncio.sleep(5)
