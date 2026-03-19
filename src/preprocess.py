import re
import pandas as pd
from config import DATA_RAW_PATH, DATA_PROCESSED_PATH


def load_data():
    df = pd.read_csv(DATA_RAW_PATH, encoding="latin-1")
    df = df[["v1", "v2"]]
    df.columns = ["label", "message"]
    df = df.dropna(subset=["message", "label"])
    return df


def clean_text(text):
    text = text.lower()
    text = text.replace("£", " gbp ").replace("$", " usd ").replace("€", " eur ")
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def encode_labels(df):
    df["label"] = df["label"].map({"ham": 0, "spam": 1})
    if df["label"].isnull().any():
        raise ValueError("Found unknown labels after encoding.")
    return df


def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates(subset="message")
    after = len(df)
    print(f"Removed {before - after} duplicates. {after} rows remaining.")
    return df


def save_processed(df):
    DATA_PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_PROCESSED_PATH, index=False)
    print(f"Cleaned data saved to: {DATA_PROCESSED_PATH}")


def preprocess():
    # For debugging, display if preprocessing is running
    print("Starting preprocessing...")
    df = load_data()
    df["message"] = df["message"].apply(clean_text)
    df = encode_labels(df)
    df = remove_duplicates(df)
    save_processed(df)
    # For debugging, display if preprocessing is completed
    print("Preprocessing completed.")
    return df


if __name__ == "__main__":
    preprocess()
