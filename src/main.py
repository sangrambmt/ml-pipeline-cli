from dotenv import load_dotenv
import os
import argparse

from ingest import load_csv, inspect_dataframe
from validate import validate_dataframe

def main() -> None:

    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="Input CSV path")

    args = parser.parse_args()

    input_path = args.input or os.getenv("INPUT_DIR") + "/sample.csv"

    print(f"Reading file: {input_path}")

    df = load_csv(input_path)
    df = validate_dataframe(df)
    inspect_dataframe(df)

if __name__ == "__main__":
    main()