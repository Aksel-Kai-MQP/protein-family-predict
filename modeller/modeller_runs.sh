#!/bin/bash

# Script to run modeller_test.py in all subdirectories of protein type folders
# This script loops through e_protein, m_protein, n_protein, and s_protein directories,
# then runs modeller_test.py in each subdirectory

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Starting modeller test runs in: $SCRIPT_DIR"
echo "=========================================="

# Loop through protein type directories, as long as they are in list
for protein_dir in "$SCRIPT_DIR"/{e_protein,m_protein,n_protein,s_protein}; do
	if [ -d "$protein_dir" ]; then
		protein_type=$(basename "$protein_dir")
		echo ""
		echo "Processing protein type: $protein_type"
		echo "========================================"
		
		# Loop through subdirectories within each protein type
		for subdir in "$protein_dir"/*/; do
			if [ -d "$subdir" ]; then
				subdir_name=$(basename "$subdir")
				echo ""
				echo "Running modeller_test.py in: $protein_type/$subdir_name"
				
				# Change to subdirectory
				cd "$subdir" || { echo "Error: Could not change to directory $subdir"; exit 1; }
				
				# Run the Python script and ignore output
				python modeller_test.py > /dev/null 2>&1
				
				# Check the exit status
				if [ $? -eq 0 ]; then
				echo "Successfully Completed: $protein_type/$subdir_name"
				else
				echo "Error Running: $protein_type/$subdir_name"
				fi
				
				# Go back to the root directory to cd again later
				cd "$SCRIPT_DIR" || { echo "Error: Could not return to directory $SCRIPT_DIR"; exit 1; }
			fi
		done
	fi
done

# Ending message
echo ""
echo "=========================================="
echo "All directories processed."
