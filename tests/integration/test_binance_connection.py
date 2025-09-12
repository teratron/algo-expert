import pytest
from algoexpert import AlgoExpert

def test_binance_connection_with_dummy_credentials():
    """
    Tests that connecting to Binance with dummy credentials raises an authentication error.
    """
    with pytest.raises(Exception):  # Replace with a more specific exception later
        expert = AlgoExpert(
            exchange="binance",
            api_key="dummy_key",
            api_secret="dummy_secret",
            base_url="",
            instrument="",
            contract="",
            mode=""
        )
        expert.balance() # This should trigger the connection and authentication
