import re
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_RAW_PATH = BASE_DIR / "data" / "spam.csv"
DATA_PROCESSED_PATH = BASE_DIR / "data" / "processed" / "sms_clean.csv"


def load_data():
    pass


def clean_text(text):
    pass


def encode_labels(df):
    pass


def remove_duplicates(df):
    pass


def save_processed(df):
    pass


def preprocess():
    pass


if __name__ == "__main__":
    preprocess()
