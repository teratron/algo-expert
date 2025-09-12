import pytest
from algoexpert import AlgoExpert
from algoexpert.exchanges.binance import BinanceAdapter
from algoexpert.exchanges.bybit import BybitAdapter

def test_algo_expert_loads_binance_adapter():
    expert = AlgoExpert(exchange="binance", api_key="", api_secret="", base_url="", instrument="", contract="", mode="")
    assert isinstance(expert.adapter, BinanceAdapter)

def test_algo_expert_loads_bybit_adapter():
    expert = AlgoExpert(exchange="bybit", api_key="", api_secret="", base_url="", instrument="", contract="", mode="")
    assert isinstance(expert.adapter, BybitAdapter)

def test_algo_expert_raises_error_for_unsupported_exchange():
    with pytest.raises(ValueError):
        AlgoExpert(exchange="unsupported", api_key="", api_secret="", base_url="", instrument="", contract="", mode="")
