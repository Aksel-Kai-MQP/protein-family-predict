import sys
import os

path = "alphafold/"
proteins_paths = ["e_proteins", "m_proteins", "n_proteins", "s_proteins"]

"""Deletes full_data_\d files in the alphafold folder,
as well as all models except model_0, and all confidence files
except for confidence_0.json, the terms of use file (per folder),
and all msa files (largest files). The archive of all alphafold data
can be found in the google drive link in the readme, and this can be used
if everything is unzipped. Should make it easier to work with the data earlier too"""

# Deletes the "full_data_\d" files in the alphafold folder
for protein_path in proteins_paths:
    sys.path.append(path + protein_path)
    # Delete files with _full_data_\d in the name
    for folders in os.listdir(path + protein_path):
        # go into each folder in path and delete files with _full_data_\d in the name
        folder_path = os.path.join(path + protein_path, folders)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                if "_full_data_" in file:
                    file_path = os.path.join(folder_path, file)
                    os.remove(file_path)
                    print(f"Deleted {file_path}")
                for num in range(1,5):
                    if file.endswith(f"model_{num}.cif") or file.endswith(f"confidences_{num}.json"):
                        file_path = os.path.join(folder_path, file)
                        os.remove(file_path)
                        print(f"Deleted {file_path}")
                if file == "terms_of_use.md":
                    file_path = os.path.join(folder_path, file)
                    os.remove(file_path)
                    print(f"Deleted {file_path}")
            if "msas" in os.listdir(folder_path):
                msa_path = os.path.join(folder_path, "msas")
                for file in os.listdir(msa_path):
                    file_path = os.path.join(msa_path, file)
                    os.remove(file_path)
                    print(f"Deleted {file_path}")
                # Delete the msas folder if it is empty
                if not os.listdir(msa_path):
                    os.rmdir(msa_path)
                    print(f"Deleted {msa_path}")

# 