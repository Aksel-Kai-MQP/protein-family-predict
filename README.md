# protein-family-predict
By Kai Davidson and Aksel Jensen

Repository for steps taken to predict and perform molecular dynamics simulations on subset of the betacoronavirus family of envelope proteins. 

Species of interest:

- Sars-CoV-2
- Sars-CoV-1
- MERS-CoV
- Bovine Coronavirus
- Murine Coronavirus
- Human Coronavirus HCoV-HKU1

## Structure

The repository structure has disjoint folders for each of the steps of the processing pipeline. Alphafold structure were ran through using [Alphafold Server](https://alphafoldserver.com/welcome). Then refined using MODELLER with template structures from known structures of Sars-CoV-2. Gromacs is being used to run molecular dynamics simulations on each protein afterwards.

```text
├── alphafold
│   ├── e_proteins
│   ├── m_proteins
│   ├── n_proteins
│   └── s_proteins
├── clean_alphafold.py
├── data
│   └── sequence_alignments
├── manifest.csv
├── modeller
│   ├── e_protein
│   ├── m_protein
│   ├── n_protein
│   └── s_protein
├── gromacs
│   └── parameters
├── README.md
└── scripts
```

## GROMACS

Before running the gromacs section of the code, which are jobs that can be dispatched with slurm. You must install the forcefield files for the CHARMM36 FF from [here](https://mackerell.umaryland.edu/charmm_ff.shtml#gromacs). We used version `charmm36-feb2026_cgenff-5.0.ff`.

All scripts used for running GROMACS simulations are in the gromacs folder. These scripts were either copied between protein species folders and each species simulation was run in its own folder, ex. `s_proteins/bovine_coronavirus/start_eq.sh`. Then some scripts were put in top level folders ex. `s_proteins` to coordinate running analysis or otherwise. Most are self-explanatory
