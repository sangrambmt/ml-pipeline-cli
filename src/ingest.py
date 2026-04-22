import os
import pandas as pd

# ingestion module
def load_csv(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise RuntimeError(f"Error reading CSV: {e}")

    if df.empty:
        raise ValueError("CSV file is empty")

    return df

# schema inspection
def inspect_dataframe(df: pd.DataFrame) -> None:
    print("\n--- Data Preview ---")
    print(df.head())

    print("\n--- Schema ---")
    print(df.dtypes)

    print("\n--- Shape ---")
    print(df.shape)