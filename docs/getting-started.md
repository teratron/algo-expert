# Getting Started

This guide will walk you through the process of installing AlgoExpert and using it to connect to cryptocurrency exchanges.

## Installation

To install the library, you can use `pip`:

```bash
pip install .
```

This will install the library and its dependencies.

If you want to contribute to the development of the library, you should install the development dependencies:

```bash
pip install .[dev]
```

## Your First Steps with AlgoExpert

Here is how to get your account balance for Binance and Bybit. You will need to have your API keys stored as environment variables.

Create a `.env` file in the root of your project with the following content:

```
BINANCE_API_KEY=your_binance_api_key
BINANCE_API_SECRET=your_binance_api_secret
BYBIT_API_KEY=your_bybit_api_key
BYBIT_API_SECRET=your_bybit_api_secret
```

Now you can use the following Python code:

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
print("Binance Balance:", balance)

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
print("Bybit Balance:", balance)
```
