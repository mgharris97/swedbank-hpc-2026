from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_RAW_PATH = BASE_DIR / "data" / "spam.csv"
DATA_PROCESSED_PATH = BASE_DIR / "data" / "processed" / "sms_clean.csv"
