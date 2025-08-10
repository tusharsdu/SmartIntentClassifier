import json
import pandas as pd
from pathlib import Path

def load_json_to_df(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    texts, labels = [], []
    for split in data:
        for item in data[split]:
            if isinstance(item, list) and len(item) >= 2:
                text, label = item[0], item[1]
                texts.append(text)
                labels.append(label)
    return pd.DataFrame({"text": texts, "label": labels})

def clean_text(text: str) -> str:
    return " ".join(text.strip().lower().split())

def save_cleaned_data(input_path: str, output_path: str):
    df = load_json_to_df(input_path)
    df["text"] = df["text"].apply(clean_text)
    df.to_csv(output_path, index=False)
    print(f"Saved cleaned data to {output_path}")

if __name__ == "__main__":
    raw = Path(__file__).resolve().parents[1] / "data" / "raw"
    processed = Path(__file__).resolve().parents[1] / "data" / "processed"
    processed.mkdir(parents=True, exist_ok=True)
    for p in raw.glob("*.json"):
        out = processed / (p.stem + ".csv")
        save_cleaned_data(str(p), str(out))
