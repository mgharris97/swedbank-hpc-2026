## HPC Cluster Setup (RTU)
>The Python version on the cluster is too old for the dependencies, so this is a workaround.

### 1. Load Python module
```bash
module load python/3.9.19
```

### 2. Clone the repo on the cluster

```bash
git clone https://github.com/mgharris97/swedbank-hpc-2026.git
cd swedbank-hpc-2026
```

### 3. Create venv and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install pandas==2.0.3 scikit-learn joblib matplotlib seaborn fastapi uvicorn wordcloud
```

### 4. Copy dataset to cluster from your local machine using SSH
> First, you will need to create an ssh key and add it to the 'credentials' section of the HPC site. [Here's a guide](https://hpc-platforma.rtu.lv/hpc.html#ssh-access)

After you can SSH into the cluster from your terminal, run the following in your terminal (repalce with your path. For example mine is: `~/Users/Matt/Documents/swedbank-hpc-2026/data/spam.csv`)

```bash
scp ~/path/to/spam.csv hpc00523@ui-2.hpc.rtu.lv:~/swedbank-hpc-2026/data/
```
