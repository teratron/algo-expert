# Plan: Logging Configuration

This plan details the steps to implement a new project-wide logging configuration.

## Phase 1: Initial Setup
1. **Define a default logging configuration:** Create a function or a dictionary that defines the default logging settings (e.g., console output, INFO level, standard format).
2. **Integrate into `AlgoExpert` initialization:** Modify the `AlgoExpert` class's `__init__` method or a dedicated setup function to apply this default logging configuration when the `AlgoExpert` instance is created.

## Phase 2: Centralized Configuration
1. **Create a `logging_config.py` module:** This module will house the logging configuration logic, including functions to set up logging based on parameters (e.g., log level, file output).
2. **Update `AlgoExpert` to use `logging_config.py`:** The `AlgoExpert` class will import and use functions from `logging_config.py` to set up logging.

## Phase 3: Trade Logging
1. **Implement a trade logger:** Create a dedicated logger for trades that outputs to a separate file.
2. **Integrate trade logging into `AlgoExpert`:** Modify the `AlgoExpert` class and exchange adapters to use the trade logger whenever a trade is executed or a transaction occurs.

## Phase 4: Example Scripts Integration
1. **Modify example scripts:** Update `examples/ema_expert_binance/expert_ema.py`, `examples/ema_expert_bybit/expert_ema.py`, and `examples/websocket_test/test_websocket.py` to use the new centralized logging configuration.

## Phase 5: Verification
1. **Run example scripts:** Execute the example scripts to ensure that logging is working as expected (console output, correct format).
2. **Test file output (optional):** If file output is implemented, verify that logs are correctly written to the specified file.
3. **Verify trade log file:** Check the dedicated trade log file for accurate and detailed trade records.

## Phase 6: Documentation
1. **Update documentation:** Add a section to the project documentation (e.g., `docs/getting-started.md`) explaining how to configure logging and how trade logging works.