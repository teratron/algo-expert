from algoexpert.exchanges.protocol import ExchangeAdapter
from algoexpert.exchanges.binance import BinanceAdapter
from algoexpert.exchanges.bybit import BybitAdapter

def test_binance_adapter_implements_protocol():
    assert issubclass(BinanceAdapter, ExchangeAdapter)

def test_bybit_adapter_implements_protocol():
    assert issubclass(BybitAdapter, ExchangeAdapter)
