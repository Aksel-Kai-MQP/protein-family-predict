#!/bin/bash
GMX="gmx"
GMXMPI="gmx"

# Clean up structure
grep -v HETATM bcovsp.B99990001.pdb >input_tmp.pdb
grep -v CONECT input_tmp.pdb >input_protein.pdb

# Generating a topology
printf "1\n0\n1\n0\n1\n0\n" | $GMX pdb2gmx -f input_protein.pdb -o input_processed.gro -water tip3p -ff "charmm36" -ter -ignh

# Defining the simulation box
$GMX editconf -f input_processed.gro -o input_newbox.gro -c -d 1.5 -bt dodecahedron

# Filling the box with water
$GMX solvate -cp input_newbox.gro -cs spc216.gro -o input_solv.gro -p topol.top

# Adding ions
touch ions.mdp
$GMX grompp -f ions.mdp -c input_solv.gro -p topol.top -o ions.tpr
yes SOL | $GMX genion -s ions.tpr -o input_solv_ions.gro -conc 0.15 -p topol.top -pname NA -nname CL -neutral

# Energy minimisation
$GMX grompp -f ./parameters/emin-charmm.mdp -c input_solv_ions.gro -p topol.top -o em.tpr
$GMXMPI mdrun -pin on -v -deffnm em

# Equilibration run - temperature
$GMX grompp -f ./parameters/nvt-charmm.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr
$GMXMPI mdrun -pin on -v -deffnm nvt

# Equilibration run - pressure
$GMX grompp -f ./parameters/npt-charmm.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.tpr
$GMXMPI mdrun -pin on -v -deffnm npt

# Prodction run
$GMX grompp -f ./parameters/md-charmm.mdp -c npt.gro -t npt.cpt -p topol.top -o md.tpr
