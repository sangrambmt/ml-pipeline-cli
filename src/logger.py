import logging
import os


def setup_logger():
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    logger = logging.getLogger()
    logger.setLevel(log_level)

    logger.handlers.clear()

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)

    # File handler
    os.makedirs("logs", exist_ok=True)
    fh = logging.FileHandler("logs/pipeline.log")
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)