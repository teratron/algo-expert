from binance.spot import Spot as SpotClient
import asyncio
import websockets
import json
import logging
from typing import List
from ..aggregator import BarAggregator

logger = logging.getLogger(__name__)

class BinanceAdapter:
    def __init__(
        self, 
        api_key: str, 
        api_secret: str, 
        base_url: str, 
        instrument: str, 
        contract: str, 
        mode: str,
        market_type: str,
        contract_type: str,
        timeframes: List[str] = ['1m']
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url if base_url else "https://api.binance.com"
        self.instrument = instrument
        self.market_type = market_type
        self.contract_type = contract_type
        self.client = SpotClient(api_key=self.api_key, api_secret=self.api_secret, base_url=self.base_url)
        
        # Initialize the bar aggregator for multiple timeframes
        self.aggregator = BarAggregator(timeframes=timeframes, on_bar_callback=self.on_bar)
        
        self.connect()

    def connect(self):
        """
        Tests the connection by making a call to the account endpoint.
        The client will raise an exception for non-2xx responses.
        """
        self.client.account()

    def balance(self):
        """
        Retrieves account balance information.
        The client will raise an exception for non-2xx responses.
        """
        return self.client.account()

    def on_init(self, *args, **kwargs):
        pass

    def on_deinit(self, *args, **kwargs):
        pass

    def on_tick(self, tick_data: dict):
        """
        Processes a new tick from the trade stream and feeds it to the aggregator.
        """
        try:
            price = float(tick_data['p'])
            quantity = float(tick_data['q'])
            timestamp_ms = int(tick_data['E'])
            
            logger.debug(f"Processing tick: Price={price}, Qty={quantity}")
            self.aggregator.add_tick(price, quantity, timestamp_ms)
        except (KeyError, ValueError) as e:
            logger.warning(f"Could not process tick data due to missing/invalid key: {e}. Data: {tick_data}")


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
        symbol = self.instrument.lower()
        trade_stream = f"{symbol}@trade"
        depth_stream = f"{symbol}@depth"
        uri = f"wss://stream.binance.com:9443/stream?streams={trade_stream}/{depth_stream}"
        
        while True:
            try:
                async with websockets.connect(uri) as websocket:
                    logger.info(f"Connected to Binance combined stream for {self.instrument}: trades and depth.")
                    while True:
                        message = await websocket.recv()
                        data = json.loads(message)
                        
                        stream = data.get("stream")
                        payload = data.get("data")

                        if not stream or not payload:
                            logger.debug(f"Received non-standard message: {data}")
                            continue

                        if stream == trade_stream:
                            self.on_tick(payload)
                        elif stream == depth_stream:
                            self.on_book(payload)
            except Exception as e:
                logger.error(f"Websocket connection failed: {e}. Reconnecting in 5 seconds...", exc_info=True)
                await asyncio.sleep(5)