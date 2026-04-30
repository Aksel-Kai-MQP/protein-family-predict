#!/bin/bash

directories=("bovine_coronavirus" "human_coronavirus_hcov_hku1" "mers_cov" "murine_coronavirus" "sars_cov_1" "sars_cov_2" "template")
analysis_dir="analysis_s"

mkdir -p "$analysis_dir"

for item in "${directories[@]}"; do
	if [ -d "$item" ]; then
		echo "Processing $item"
		cp "$item/gyrate.xvg" "$analysis_dir/${item}_gyrate.xvg"
		cp "$item/rmsd.xvg" "$analysis_dir/${item}_rmsd.xvg"
		cp "$item/rmsf.xvg" "$analysis_dir/${item}_rmsf.xvg"
	else
		echo "Directory $item not found."
	fi
done

zip "$analysis_dir.zip" -r "$analysis_dir"
