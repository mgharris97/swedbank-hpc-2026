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
| pandas | Data loading and manipulation |
| scikit-learn | ML model training and evaluation (Logistic Regression, Random Forest, etc.) |
| FastAPI | API endpoint |
| uvicorn | Server for running FastAPI |
| joblib | Model serialization and loading |

## To setup on your end...

### 1. Clone the repository
```bash
git clone https://github.com/mgharris97/swedbank-hpc-2026.git
cd swedbank-hpc-2026
```

### 2. Create aand activate the virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
   On Windows
```bash
 venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the dataset
Download the SMS dataset from Kaggle and place it in the `data/` folder.

https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset





