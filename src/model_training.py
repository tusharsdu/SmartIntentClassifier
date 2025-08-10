import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from pathlib import Path

def train_model(data_path: str, model_path: str):
    df = pd.read_csv(data_path)
    X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)
    pipeline = Pipeline([("tfidf", TfidfVectorizer()), ("clf", LogisticRegression(max_iter=1000))])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {acc*100:.2f}%")
    joblib.dump(pipeline, model_path)
    print(f"Model saved at {model_path}")
    return acc

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    processed = root / "data" / "processed"
    models = root / "models"
    models.mkdir(parents=True, exist_ok=True)
    csvs = list(processed.glob("*.csv"))
    if not csvs:
        print("No processed CSV found. Run data cleaning first.")
    else:
        train_model(str(csvs[0]), str(models / "intent_classifier.pkl"))
