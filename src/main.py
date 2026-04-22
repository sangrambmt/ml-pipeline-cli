from dotenv import load_dotenv
import os
import argparse
import logging

from ingest import load_csv, inspect_dataframe
from validate import validate_dataframe
from logger import setup_logger

logger = logging.getLogger(__name__)


def main() -> None:
    load_dotenv()
    setup_logger()

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str)

    args = parser.parse_args()

    input_dir = os.getenv("INPUT_DIR", "data/raw")
    input_path = args.input or os.path.join(input_dir, "sample.csv")

    if not input_path.endswith(".csv"):
        logger.error("Invalid file type")
        raise ValueError("Only CSV files are supported")

    logger.info(f"Starting pipeline for file: {input_path}")

    df = load_csv(input_path)
    df = validate_dataframe(df)
    inspect_dataframe(df)

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    main()