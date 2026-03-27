## Swedbank HPC Fraud Detection Challenge

ML-powered SMS fraud detection system built with pandas, scikit-learn, fastAPI, and trained on RTU's HPC cluster. Developed in collaboration with Ģirts Bērziņš of Swedbank as part of RTU's HPC challenge 2026.

### Participants:

    Matthew Harris
    Ayma Rehman
    Klints Legranžs
    Evelīna Šadurska
### Tech Stack

| Library | Purpose |
|---|---|
| numpy | Numerical operations and array handling |
| pandas | Data loading and manipulation |
| scikit-learn | ML model training and evaluation (Logistic Regression, Random Forest, etc.) |
| matplotlib | Data visualization |
| seaborn | Statistical data visualization |
| FastAPI | API endpoint |
| uvicorn | Server for running FastAPI |
| joblib | Model serialization and loading |

## To set up on your end...

### 1. Clone the repository
```bash
git clone https://github.com/mgharris97/swedbank-hpc-2026.git
cd swedbank-hpc-2026
```

### 2. Create and activate the virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
   On Windows: ```venv\Scripts\activate```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the dataset
Download the SMS dataset from Kaggle and place it in the `data/` folder locally on your computer 

[UC Irvine SMS Spam Collection Dataset from Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)

### 5. Preprocess the data
```bash
python src/preprocess.py
```

### 6. Train the model
```bash
python src/model.py
```

### Note:
Keep in mind, every time you come back to work on this project, you need to reactivate the venv first: ```source venv/bin/activate ```

Your directory structure should look like this :)

```
.
├── data
│   ├── processed
│   └── spam.csv
├── hpc
│   ├── grid_search.md
│   ├── grid_search.sh
│   ├── results
│   └── setup.md
├── models
│   ├── model.pkl
│   └── vectorizer.pkl
├── notebooks
│   └── eda.ipynb
├── requirements.txt
├── src
│   ├── api.py
│   ├── config.py
│   ├── evaluate.py
│   ├── grid_search.py
│   ├── model.py
│   └── preprocess.py
├── venv
├── LICENSE
└── README.md
```

