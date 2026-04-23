import logging

logger = logging.getLogger(__name__)

EXPECTED_SCHEMA = {
    "id": "int64",
    "name": "object",
    "age": "float64",
    "city": "object",
}


def validate_schema(df):
    missing = set(EXPECTED_SCHEMA) - set(df.columns)

    if missing:
        logger.error(f"Missing columns: {missing}")
        raise ValueError(missing)

    for col, dtype in EXPECTED_SCHEMA.items():
        try:
            df[col] = df[col].astype(dtype)
        except Exception:
            logger.exception(f"Type conversion failed for column: {col}")
            raise


def handle_nulls(df):
    null_cells = df.isnull().sum().sum()
    null_rows = df.isnull().any(axis=1).sum()

    if null_cells > 0:
        logger.warning(f"Null cells found: {null_cells}")
        logger.warning(f"Rows containing nulls: {null_rows}")
        logger.info(f"Null count by column:\n{df.isnull().sum()}")

        df = df.dropna()
        logger.info(f"Shape after null removal: {df.shape}")

    return df


def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates()
    removed = before - len(df)

    logger.info(f"Duplicates removed: {removed}")
    return df


def validate_dataframe(df):
    logger.info("Starting validation stage")

    validate_schema(df)
    df = handle_nulls(df)
    df = remove_duplicates(df)

    logger.info("Validation stage completed")
    return df