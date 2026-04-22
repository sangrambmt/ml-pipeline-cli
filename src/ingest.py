import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def load_csv(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(file_path)

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        logger.exception("CSV read failed")
        raise RuntimeError(e)

    if df.empty:
        logger.warning("CSV is empty")
        raise ValueError("Empty CSV")

    logger.info(f"Loaded data shape: {df.shape}")
    logger.info(f"Columns: {list(df.columns)}")

    return df


def inspect_dataframe(df: pd.DataFrame) -> None:
    logger.info("Inspecting dataframe")
    logger.info(f"\nPreview:\n{df.head()}")
    logger.info(f"\nSchema:\n{df.dtypes}")
    logger.info(f"\nShape: {df.shape}")