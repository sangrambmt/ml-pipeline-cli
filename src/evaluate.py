import json
import logging
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import joblib

logger = logging.getLogger(__name__)


def evaluate_model(data_path: str, model_path: str, metrics_path: str):
    df = pd.read_csv(data_path)

    X = df[["age"]]
    y_true = df["id"]

    model = joblib.load(model_path)
    y_pred = model.predict(X)

    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    metrics = {
        "mse": float(mse),
        "r2": float(r2)
    }

    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)

    logger.info(f"Evaluation metrics saved to {metrics_path}")