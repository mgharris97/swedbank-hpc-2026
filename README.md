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
Download the SMS dataset from Kaggle and place it in the `data/` folder.

[SMS Spam Collection Dataset](https://archive.ics.uci.edu/dataset/228/sms+spam+collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection))

### Note:
Keep in mind, every time you come back to work on this project, you need to reactivate the venv first: ```source venv/bin/activate ```







