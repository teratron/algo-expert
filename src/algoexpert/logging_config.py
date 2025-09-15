import logging
import sys

def setup_logging(level=logging.INFO, log_file=None):
    """
    Sets up the default logging configuration for the project.
    Logs to console with a standardized format.
    Optionally logs to a file.
    """
    # Ensure the root logger is configured only once
    if not logging.root.handlers:
        handlers = [
            logging.StreamHandler(sys.stdout)
        ]
        if log_file:
            handlers.append(logging.FileHandler(log_file))

        logging.basicConfig(
            level=level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=handlers
        )

    # Set default logging level for 'algoexpert' modules
    logging.getLogger('algoexpert').setLevel(level)

def setup_trade_logging(trade_log_file, level=logging.INFO):
    """
    Sets up a dedicated logger for trade events.
    Logs to a specified file with a standardized format.
    """
    trade_logger = logging.getLogger('algoexpert.trades')
    trade_logger.setLevel(level)
    trade_logger.propagate = False  # Prevent logs from going to the root logger

    if not trade_logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(trade_log_file)
        file_handler.setFormatter(formatter)
        trade_logger.addHandler(file_handler)

    return trade_logger
