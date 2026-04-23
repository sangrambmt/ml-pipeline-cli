from dotenv import load_dotenv
import os
import argparse
import logging

from ingest import load_csv, inspect_dataframe
from validate import validate_dataframe
from logger import setup_logger
from train import train_model
from evaluate import evaluate_model

logger = logging.getLogger(__name__)


def main() -> None:
    load_dotenv()
    setup_logger()

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str)

    args = parser.parse_args()

    input_dir = os.getenv("INPUT_DIR", "data/raw")
    output_dir = os.getenv("OUTPUT_DIR", "data/processed")

    input_path = args.input or os.path.join(input_dir, "sample.csv")

    logger.info(f"Pipeline config: input_path={input_path}, output_dir={output_dir}")

    if not input_path.endswith(".csv"):
        logger.error("Invalid file type")
        raise ValueError("Only CSV files are supported")

    logger.info(f"Starting pipeline for file: {input_path}")

    # Step 1 — Load
    df = load_csv(input_path)

    # Step 2 — Validate
    df = validate_dataframe(df)

    # Step 3 — Save cleaned data
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "clean.csv")

    df.to_csv(output_path, index=False)
    logger.info(f"Saved cleaned data to {output_path}")

    # Step 4 — Train model
    model_dir = "models"
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.pkl")

    train_model(output_path, model_path)

    # Step 5 — Evaluate model
    metrics_dir = "metrics"
    os.makedirs(metrics_dir, exist_ok=True)
    metrics_path = os.path.join(metrics_dir, "metrics.json")

    evaluate_model(output_path, model_path, metrics_path)

    # Step 6 — Inspect (optional)
    inspect_dataframe(df)

    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    main()