EXPECTED_SCHEMA = {
    "id": "int64",
    "name": "object",
    "age": "float64",
    "city": "object",
}


# Schema validation + type enforcement
def validate_schema(df):
    missing_cols = set(EXPECTED_SCHEMA.keys()) - set(df.columns)

    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")

    for col, expected_type in EXPECTED_SCHEMA.items():
        try:
            df[col] = df[col].astype(expected_type)
        except Exception:
            raise TypeError(
                f"Column '{col}' cannot be converted to {expected_type}, got {df[col].dtype}"
            )


# Null handling
def handle_nulls(df):
    if df.isnull().sum().sum() > 0:
        print("Null values found. Dropping rows with nulls.")
        df = df.dropna()
    return df


# Duplicate handling
def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print(f"Removed {before - after} duplicate rows.")
    return df


# Combined validation pipeline
def validate_dataframe(df):
    validate_schema(df)
    df = handle_nulls(df)
    df = remove_duplicates(df)
    return df