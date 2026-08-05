# src/app_logging/logger.py

import logging

try:
    from rich.logging import RichHandler
    HAS_RICH = True
except ImportError:
    HAS_RICH = False


def setup_logger(debug: bool = False):
    """
    Setup the logger for the application with graceful fallback for Pyodide web runtime.
    """
    level = logging.DEBUG if debug else logging.INFO

    if HAS_RICH:
        handlers = [RichHandler(rich_tracebacks=True, markup=True, show_path=True)]
        logging.basicConfig(
            level=level,
            format="%(message)s",
            datefmt="[%X]",
            handlers=handlers
        )
    else:
        logging.basicConfig(
            level=level,
            format="%(asctime)s [%(levelname)s] %(message)s",
            datefmt="[%X]",
            handlers=[logging.StreamHandler()]
        )

    return logging.getLogger("app")


if __name__ == "__main__":
    logger = setup_logger(debug=True)

    logger.info("Hello, World!")
    logger.debug("App Debugging!")
    logger.warning("App Warning!")
    logger.error("App Error!")
    logger.critical("App Critical!")