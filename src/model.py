import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
from config import DATA_PROCESSED_PATH, MODELS_DIR


def train():
    MODELS_DIR.mkdir(exist_ok=True)
    # Comments for Matt so he knows what is happening
    # pandas: loading cleaned CSV
    # train_test_split: splits data into training and testing portions
    #   data is split into training and testing so the model does not train on 100% of data so it can
    #   classify a message it has not seen before
    # TfdfVectorizer: converts texts messages into numbers
    # joblib: saves the trained model to disk so it does not need to be retrained every time

    # load cleaned dataset
    df = pd.read_csv(DATA_PROCESSED_PATH)

    # Drop any rows where message is empty
    df = df.dropna(subset=["message"])

    X = df["message"]  # the sms text
    y = df["label"]  # 0 = ham, 1 = spam

    # 80/20 split (80% training, 20% testing) between messages (X) and labels (y)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # TfidfVectorizer con`verts text messages into numbers the model can understand
    vectorizer = TfidfVectorizer()

    # fit = vectorizer reads all messages, and builds a vocab. Every unique word gets assigned a num.
    # transform = converts messages into numbers using the vocabulary
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    joblib.dump(model, MODELS_DIR / "model.pkl")
    joblib.dump(vectorizer, MODELS_DIR / "vectorizer.pkl")

    print("Model and vectorizer saved to models/")
    print(f"Training set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}")


if __name__ == "__main__":
    train()
