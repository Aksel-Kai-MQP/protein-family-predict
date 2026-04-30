#!/bin/bash

directories=("bovine_coronavirus" "human_coronavirus_hcov_hku1" "mers_cov" "murine_coronavirus" "sars_cov_1" "sars_cov_2" "template_20ns")
analysis_dir="gromacs_center_s"

mkdir -p "$analysis_dir"

for item in "${directories[@]}"; do
	if [ -d "$item" ]; then
		echo "Processing $item"
		cp "$item/md_last_center.pdb" "$analysis_dir/${item}_s_prot_md_center.gro"
	else
		echo "Directory $item not found."
	fi
done

zip "$analysis_dir.zip" -r "$analysis_dir"
