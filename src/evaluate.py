import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from config import DATA_PROCESSED_PATH, MODELS_DIR


def evaluate():
    df = pd.read_csv(DATA_PROCESSED_PATH)
    df = df.dropna(subset=["message"])
    X = df["message"]  # Features (input): text messages
    y = df["label"]  # Target (output): 0 = ham, 1 = spam

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = joblib.load(MODELS_DIR / "model.pkl")
    vectorizer = joblib.load(MODELS_DIR / "vectorizer.pkl")

    X_test_vec = vectorizer.transform(X_test)
    y_pred = model.predict(X_test_vec)

    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=["Ham", "Spam"]))

    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Ham", "Spam"],
        yticklabels=["Ham", "Spam"],
    )
    plt.title("Confusion Matrix")
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    evaluate()
