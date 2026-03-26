import time
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from pathlib import Path
from config import DATA_PROCESSED_PATH, MODELS_DIR

df = pd.read_csv(DATA_PROCESSED_PATH)
df = df.dropna(subset=['message'])

X = df['message']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Define models and parameter grids
models = {
    'LogisticRegression': {
        'model': LogisticRegression(max_iter=1000),
        'params': {
            'C': [0.01, 0.1, 1, 10, 100, 1000],
            'solver': ['lbfgs', 'liblinear', 'saga'],
            'penalty': ['l1', 'l2']
        }
    },
    'NaiveBayes': {
        'model': MultinomialNB(),
        'params': {
            'alpha': [0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0]
        }
    },
    'SVM': {
        'model': LinearSVC(max_iter=2000),
        'params': {
            'C': [0.01, 0.1, 1, 10, 100, 1000],
            'loss': ['hinge', 'squared_hinge'],
            'tol': [1e-4, 1e-3, 1e-2]
        }
    },
    'RandomForest': {
        'model': RandomForestClassifier(),
        'params': {
            'n_estimators': [100, 200, 300, 500, 1000],
            'max_depth': [None, 5, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'max_features': ['sqrt', 'log2']
        }
    }
}

# Run grid search 
results = []

for name, config in models.items():
    print(f"\nRunning grid search for {name}...")

    start_time = time.time() # record how long each model takes

    # n_jobs=-1 uses all available CPU cores simultaneously which is what makes the HPC usable
    # cv=10 means 10 fold cross validation
    grid_search = GridSearchCV(
        config['model'],
        config['params'],
        cv=10,
        n_jobs=-1,
        scoring='f1'
    )

    grid_search.fit(X_train_vec, y_train)

    elapsed = time.time() - start_time

    results.append({
        'model': name,
        'best_score': round(grid_search.best_score_ * 100, 2),
        'best_params': grid_search.best_params_,
        'time_seconds': round(elapsed, 2)
    })

    print(f"{name} done in {elapsed:.2f}s — Best F1: {grid_search.best_score_:.4f}")

# Print results
print("\n" + "="*60)
print("GRID SEARCH RESULTS")
print("="*60)

for r in results:
    print(f"\n{r['model']}")
    print(f"  Best F1 Score: {r['best_score']}%")
    print(f"  Best Params:   {r['best_params']}")
    print(f"  Time:          {r['time_seconds']}s")

# Save the best model (the one with the highest F1 score)
best = max(results, key=lambda x: x['best_score'])
print(f"\nBest overall model: {best['model']} with F1 of {best['best_score']}%")

# Save results to file for presentation
results_dir = Path(__file__).resolve().parent.parent / 'hpc' / 'results'
results_dir.mkdir(exist_ok=True)

with open(results_dir / 'grid_search_results.txt', 'w') as f:
    for r in results:
        f.write(f"{r['model']}\n")
        f.write(f"  Best F1 Score: {r['best_score']}%\n")
        f.write(f"  Best Params:   {r['best_params']}\n")
        f.write(f"  Time:          {r['time_seconds']}s\n\n")