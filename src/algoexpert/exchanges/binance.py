import time
import hmac
import hashlib
import requests

class BinanceAdapter:
    def __init__(self, api_key: str, api_secret: str, base_url: str, instrument: str, contract: str, mode: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url if base_url else "https://api.binance.com"
        self.connect()

    def connect(self):
        timestamp = int(time.time() * 1000)
        query_string = f"timestamp={timestamp}"
        signature = hmac.new(self.api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
        url = f"{self.base_url}/api/v3/account?{query_string}&signature={signature}"
        headers = {'X-MBX-APIKEY': self.api_key}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will raise an exception for non-2xx responses

    def balance(self):
        timestamp = int(time.time() * 1000)
        query_string = f"timestamp={timestamp}"
        signature = hmac.new(self.api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
        url = f"{self.base_url}/api/v3/account?{query_string}&signature={signature}"
        headers = {'X-MBX-APIKEY': self.api_key}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will raise an exception for non-2xx responses
        return response.json()

    def on_init(self, *args, **kwargs):
        pass

    def on_deinit(self, *args, **kwargs):
        pass

    def on_tick(self, *args, **kwargs):
        pass

    def on_bar(self, *args, **kwargs):
        pass

    def on_timer(self, *args, **kwargs):
        pass

    def on_trade(self, *args, **kwargs):
        pass

    def on_transaction(self, *args, **kwargs):
        pass

    def on_book(self, *args, **kwargs):
        pass

    def run(self):
        pass