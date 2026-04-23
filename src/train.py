import os
import logging
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

logger = logging.getLogger(__name__)


def train_model(input_path: str, model_path: str):
    df = pd.read_csv(input_path)

    # simple feature selection
    X = df[["age"]]
    y = df["id"]

    model = LinearRegression()
    model.fit(X, y)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)

    logger.info(f"Model trained and saved to {model_path}")