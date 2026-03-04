import os
import csv
import re
from pathlib import Path
from Bio.PDB import MMCIFParser, PDBIO

# ONLY RUN THIS ONCE

manifest_path = "manifest.csv"
alphafold_dir = "alphafold"

def normalize_name(name):
    """Lowercase name and replace spaces/dashes with underscores"""
    return name.lower().replace(" ", "_").replace("-", "_")

# Read manifest csv file using proper CSV parser
with open(manifest_path, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        species = row["Species"]
        protein_name = row["Protein Name"]
        
        # Normalize species and protein names
        normalized_species = normalize_name(species)
        normalized_protein = normalize_name(protein_name)
        
        # Create directory for protein type if it doesn't exist
        protein_dir = os.path.join("modeller", normalized_protein)
        if not os.path.exists(protein_dir):
            os.makedirs(protein_dir)
            print(f"Created directory: {protein_dir}")
        
        # Create directory for species if it doesn't exist
        species_dir = os.path.join(protein_dir, normalized_species)
        if not os.path.exists(species_dir):
            os.makedirs(species_dir)
            print(f"Created directory: {species_dir}")

# AlphaFold naming convention for species mapping
alphafold_naming = ["bovine", "mers", "cov_1", "hku1", "murine", "cov_2"]

# Protein type mapping (folder name prefix to normalized name)
protein_types = {
    "e_proteins": "e_protein",
    "m_proteins": "m_protein",
    "n_proteins": "n_protein",
    "s_proteins": "s_protein"
}

# Convert CIF files to PDB and place in modeller directories
parser = MMCIFParser()
pdb_io = PDBIO()

for protein_folder, protein_norm in protein_types.items():
    protein_path = os.path.join(alphafold_dir, protein_folder)
    if not os.path.exists(protein_path):
        continue
    
    # Find all folders in this protein type directory
    for folder in os.listdir(protein_path):
        folder_path = os.path.join(protein_path, folder)
        if not os.path.isdir(folder_path):
            continue
        
        # Look for model_0.cif file
        cif_file = None
        for file in os.listdir(folder_path):
            if file.endswith("_model_0.cif"):
                cif_file = os.path.join(folder_path, file)
                break
        
        if cif_file is None:
            continue
        
        species_found = None
        for species_key in alphafold_naming:
            if species_key in folder.lower():
                # Map alphafold_naming to normalized species names
                species_mapping = {
                    "bovine": "bovine_coronavirus",
                    "mers": "mers_cov",
                    "cov_1": "sars_cov_1",
                    "hku1": "human_coronavirus_hcov_hku1",
                    "murine": "murine_coronavirus",
                    "cov_2": "sars_cov_2"
                }
                species_found = species_mapping.get(species_key)
                break
        
        if species_found is None:
            print(f"Warning: Could not determine species for {folder}")
            continue
        
        # Build output path
        output_dir = os.path.join("modeller", protein_norm, species_found)
        if not os.path.exists(output_dir):
            print(f"Warning: Output directory does not exist: {output_dir}")
            continue
        
        # Convert CIF to PDB for MODELLER and GROMACS compatibility
        try:
            structure = parser.get_structure(folder, cif_file)
            output_pdb = os.path.join(output_dir, f"{species_found}_{protein_norm}.pdb")
            pdb_io.set_structure(structure)
            pdb_io.save(output_pdb)
            print(f"Converted: {cif_file} -> {output_pdb}")
        except Exception as e:
            print(f"Error converting {cif_file}: {e}")

