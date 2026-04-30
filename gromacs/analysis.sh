#!/bin/bash

#SBATCH -p short
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --time=04:00:00
#SBATCH -o analysis.o
#SBATCH -e analysis.e
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=<YOUR EMAIL>
#SBATCH -J gromacs_sc2sp_analysis

module unload cudnn8.5-cuda11.7
module unload cuda11.7
module load cuda12.2
module load cudnn8.9-cuda12.2
source ~/software/gromacs/bin/GMXRC
GMX="gmx"

echo "1 0" | $GMX trjconv -s md.tpr -f md.xtc -o md_cluster.xtc -pbc cluster

echo "0" | $GMX trjconv -s md.tpr -f md_cluster.xtc -o md_nojump.xtc -pbc nojump

echo "1 0" | $GMX trjconv -s md.tpr -f md_nojump.xtc -o md_center.xtc -pbc mol -center -ur compact

echo "4 4" | $GMX rms -s md.tpr -f md_center.xtc -o rmsd.xvg -tu ns

echo "4" | $GMX rmsf -s md.tpr -f md_center.xtc -o rmsf.xvg -res

echo "1" | $GMX gyrate -s md.tpr -f md_center.xtc -o gyrate.xvg -sel Protein -tu ns
