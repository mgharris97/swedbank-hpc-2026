# HPC Cluster Setup (RTU)

> This guide explains how to set up the environment and run Python jobs on the RTU HPC cluster.

---

## 1. Connect to the Cluster

### Option A: SSH (Recommended)

Before connecting, ensure your SSH key is added via the HPC platform.

```bash
ssh yourusername@ui-2.hpc.rtu.lv
```

### Option B: Web Interface

You can also access a terminal via the RTU OnDemand portal:
https://ood.hpc.rtu.lv/

---

## 2. Load Python Module

The default system Python is outdated and not usable for this project. Load a newer version:

```bash
module load python/3.9.19
```

Verify:

```bash
python3 --version
```

---

## 3. Clone the Repository

```bash
git clone https://github.com/mgharris97/swedbank-hpc-2026.git
cd swedbank-hpc-2026
```

---

## 4. Create Virtual Environment and Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install pandas==2.0.3 scikit-learn joblib matplotlib seaborn fastapi uvicorn wordcloud
```

---

## 5. Copy Dataset to Cluster

> You must have SSH access configured first.

From your local machine:

```bash
scp ~/path/to/spam.csv yourusername@ui-2.hpc.rtu.lv:~/swedbank-hpc-2026/data/
```

---

## 6. Running Jobs on the HPC Cluster

Python scripts must be executed using the cluster's job scheduler.

### Job Scheduler

The RTU HPC cluster uses a **PBS/Torque-based scheduler**.

Common commands:

* `qsub` → submit job
* `qstat` → check job status

---

## 7. Example: Hello World Job

### 7.1 Create Python Script

```bash
nano helloworld.py
```

```python
print("Hello, world!")
```

---

### 7.2 Create Job Script

```bash
nano hello_job.sh
```

```bash
#!/bin/bash
#PBS -N hello_job
#PBS -l walltime=00:01:00
#PBS -l select=1:ncpus=1
#PBS -j oe
#PBS -o output.txt

cd $PBS_O_WORKDIR

module load python/3.9.19
python3 helloworld.py
```

---

### 7.3 Submit Job

```bash
qsub hello_job.sh
```

You will receive a job ID (e.g., `5283253.rudens`).

---

### 7.4 Check Job Status

```bash
qstat
```

Job states:

* `Q` = queued
* `R` = running
* `C` = completed

---

### 7.5 View Output

```bash
cat output.txt
```

Expected result:

```
Hello, world!
```

---

## Summary

1. Connect to the cluster
2. Load Python module
3. Clone repository
4. Set up virtual environment
5. Upload dataset
6. Create job script
7. Submit with `qsub`
8. Check results

---
