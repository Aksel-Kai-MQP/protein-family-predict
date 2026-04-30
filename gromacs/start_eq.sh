#!/bin/bash

#SBATCH -p short
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --gpus-per-node=1
#SBATCH --gres=gpu:1
#SBATCH -C "L40S"
#SBATCH --time=23:59:59
#SBATCH -o job.o
#SBATCH -e job.e
#SBATCH --mail-type=all
#SBATCH --mail-user=<YOUR EMAIL>
#SBATCH -J gromacs_sc2sp_eq
module unload cudnn8.5-cuda11.7
module unload cuda11.7
module load cuda12.2
module load cudnn8.9-cuda12.2
source ~/software/gromacs/bin/GMXRC
GMX="gmx"
bash run_md_eq.sh >run_eq_out.log 2>run_eq_error.log
touch run_md_out.log
touch run_md_error.log
sbatch start.sh
