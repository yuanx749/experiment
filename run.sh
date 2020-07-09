#!/bin/bash -l

#SBATCH -A [project name]
#SBATCH -p core
#SBATCH -n 1
#SBATCH -t 1-00:00:00
#SBATCH -o "./slurm/slurm-%j.out"

log_file=./logs/$(date +%Y%m%d-%H%M%S).log
python -u ${1} 2>&1 | tee $log_file