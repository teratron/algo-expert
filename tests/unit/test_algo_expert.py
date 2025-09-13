import pytest
from unittest.mock import patch, MagicMock
from algoexpert import AlgoExpert

def test_algo_expert_unsupported_exchange():
    with pytest.raises(ValueError, match="Unsupported exchange: noname"):
        AlgoExpert(exchange="noname", api_key="", api_secret="", base_url="", instrument="", contract="", mode="")

@patch('algoexpert.exchanges.binance.BinanceAdapter')
def test_algo_expert_initializes_binance_adapter(mock_adapter):
    expert = AlgoExpert(exchange="binance", api_key="key", api_secret="secret", base_url="url", instrument="inst", contract="cont", mode="mode")
    mock_adapter.assert_called_once_with(api_key="key", api_secret="secret", base_url="url", instrument="inst", contract="cont", mode="mode")
    assert expert.adapter == mock_adapter.return_value

@patch('algoexpert.exchanges.bybit.BybitAdapter')
def test_algo_expert_initializes_bybit_adapter(mock_adapter):
    expert = AlgoExpert(exchange="bybit", api_key="key", api_secret="secret", base_url="url", instrument="inst", contract="cont", mode="mode")
    mock_adapter.assert_called_once_with(api_key="key", api_secret="secret", base_url="url", instrument="inst", contract="cont", mode="mode")
    assert expert.adapter == mock_adapter.return_value

@pytest.mark.parametrize("method_name, args, kwargs", [
    ("balance", (), {}),
    ("on_init", (1, 2), {"a": 3}),
    ("on_deinit", (), {}),
    ("on_tick", (1,), {}),
    ("on_bar", (2,), {}),
    ("on_timer", (), {"b": 4}),
    ("on_trade", (3,), {}),
    ("on_transaction", (4,), {}),
    ("on_book", (5,), {}),
    ("run", (), {}),
])
@patch('algoexpert.exchanges.binance.BinanceAdapter')
def test_algo_expert_calls_adapter_methods(mock_adapter, method_name, args, kwargs):
    expert = AlgoExpert(exchange="binance", api_key="key", api_secret="secret", base_url="url", instrument="inst", contract="cont", mode="mode")
    adapter_instance = mock_adapter.return_value
    method_to_call = getattr(expert, method_name)
    method_to_call(*args, **kwargs)
    mock_method = getattr(adapter_instance, method_name)
    mock_method.assert_called_once_with(*args, **kwargs)