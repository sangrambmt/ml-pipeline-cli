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

    os.makedirs("logs", exist_ok=True)

    ch = logging.StreamHandler()
    fh = logging.FileHandler("logs/pipeline.log")

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)