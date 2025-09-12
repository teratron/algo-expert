import time
import hmac
import hashlib
import requests

class BybitAdapter:
    def __init__(self, api_key: str, api_secret: str, base_url: str, instrument: str, contract: str, mode: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url if base_url else "https://api.bybit.com"

    def balance(self):
        timestamp = int(time.time() * 1000)
        recv_window = 5000
        query_string = "accountType=UNIFIED"
        string_to_sign = str(timestamp) + self.api_key + str(recv_window) + query_string
        signature = hmac.new(self.api_secret.encode('utf-8'), string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()
        url = f"{self.base_url}/v5/account/wallet-balance?{query_string}"
        headers = {
            'X-BAPI-API-KEY': self.api_key,
            'X-BAPI-TIMESTAMP': str(timestamp),
            'X-BAPI-RECV-WINDOW': str(recv_window),
            'X-BAPI-SIGN': signature,
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()