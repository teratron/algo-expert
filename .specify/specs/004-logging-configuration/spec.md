# Specification: Logging Configuration

This specification outlines the requirements for implementing a new project-wide logging configuration.

## Goals
- Centralized logging configuration for all modules.
- Flexible logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- Output to console by default.
- Option to output to a file.
- Standardized log format.
- Record all trades to a dedicated file.

## Details
- The logging configuration should be set up once at the application's entry point.
- All modules should use Python's standard `logging` module.
- The configuration should be easily modifiable.
- Log messages should include timestamp, log level, module name, and the message itself.
- Trade records should include relevant trade details (e.g., symbol, price, quantity, type, timestamp).

## Acceptance Criteria
- All modules within the `algoexpert` library and example scripts use the new logging configuration.
- Logging levels can be changed easily.
- Logs are displayed in the console.
- Logs can optionally be saved to a file.
- All executed trades are recorded to a separate log file with detailed information.