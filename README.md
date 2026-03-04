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
├── README.md
└── scripts
```
