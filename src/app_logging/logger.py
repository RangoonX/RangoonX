# src/app_logging/logger.py

import logging


def setup_logger(debug: bool = False):
    """
    Setup the logger for the application using standard Python logging.
    100% Pyodide and Web WASM compatible without external dependencies.
    """
    level = logging.DEBUG if debug else logging.INFO

    logger = logging.getLogger("app")
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="[%X]")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)

    return logger


if __name__ == "__main__":
    logger = setup_logger(debug=True)
    logger.info("App logger initialized.")