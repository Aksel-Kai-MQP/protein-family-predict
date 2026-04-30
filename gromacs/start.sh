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
#SBATCH -J gromacs_sc2sp
module unload cudnn8.5-cuda11.7
module unload cuda11.7
module load cuda12.2
module load cudnn8.9-cuda12.2
source ~/software/gromacs/bin/GMXRC
GMX="gmx"
GMXMPI="gmx"
$GMXMPI mdrun -pin on -v -cpi md.cpt -deffnm md -maxh 24 >>run_md_out.log 2>>run_md_error.log
TIME_LEFT=$(squeue -h -j "$SLURM_JOB_ID" -O TimeLeft | awk -F':|-' '{
    if (NF == 1) {print $NF}
    else if (NF == 2) {print ($1 * 60) + $2}
    else if (NF == 3) {print ($1 * 3600) + ($2 * 60) + $3}
    else if (NF == 4) {print ($1 * 86400) + ($2 * 3600) + ($3 * 60) + $4}
}')
echo "TIME_LEFT=$TIME_LEFT"
if [ "$TIME_LEFT" -lt 1200 ]; then
  sbatch start.sh
fi

