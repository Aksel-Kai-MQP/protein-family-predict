directories=("bovine_coronavirus" "human_coronavirus_hcov_hku1" "mers_cov" "murine_coronavirus" "sars_cov_1" "sars_cov_2" "template")
analysis_dir="analysis_s"

mkdir -p "$analysis_dir"

for item in "${directories[@]}"; do
	if [ -d "$item" ]; then
		echo "Running $item"
		id=$(sbatch --parsable -D "$item" "$item/analysis.sh")
	else
		echo "Directory $item not found."
	fi
done
