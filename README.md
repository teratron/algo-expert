# AlgoExpert: Algorithmic Trading Library

## Description

`AlgoExpert` is a Python library for algorithmic trading that provides a unified interface for interacting with different cryptocurrency exchanges.

## Installation

To install the library, you can use `pip`:

```bash
pip install .
```

To install the development dependencies, run:

```bash
pip install .[dev]
```

## Usage

Here is how to get your account balance for Binance and Bybit:

```python
from algoexpert import AlgoExpert
import os
from dotenv import load_dotenv

load_dotenv()

# For Binance
binance_expert = AlgoExpert(
    exchange="binance",
    api_key=os.getenv("BINANCE_API_KEY"),
    api_secret=os.getenv("BINANCE_API_SECRET"),
    base_url="https://api.binance.com",
    instrument="",
    contract="",
    mode=""
)

balance = binance_expert.balance()
print(balance)

# For Bybit
bybit_expert = AlgoExpert(
    exchange="bybit",
    api_key=os.getenv("BYBIT_API_KEY"),
    api_secret=os.getenv("BYBIT_API_SECRET"),
    base_url="https://api.bybit.com",
    instrument="",
    contract="",
    mode=""
)

balance = bybit_expert.balance()
print(balance)
```
