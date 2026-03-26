#!/bin/bash
#PBS -N grid_search
#PBS -l walltime=02:00:00
#PBS -l nodes=1:ppn=16
#PBS -j oe
#PBS -o /mnt/home/hpc00523/swedbank-hpc-2026/hpc/results/grid_search_output.txt
#PBS -A hpc_mt_00f65_hpcallocforgroup

cd $PBS_O_WORKDIR

module load python/3.9.19
source venv/bin/activate

echo "Job started: $(date)"
echo "Running on: $(hostname)"
echo "CPUs requested: 16"

export OMP_NUM_THREADS=16
export MKL_NUM_THREADS=16
export NUMEXPR_NUM_THREADS=16
python src/grid_search.py

echo "Job finished: $(date)" 