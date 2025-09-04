#!/bin/bash
# print greeting message
# echo "Hello, World"
# accessions=("stuff","list")

echo "Retrieving sequences from NCBI..."
echo "Running python script..."

python3 ncbi_sequences.py
if [ $? -eq 0 ]; then
    echo "Python script executed successfully."
else
    echo "Python script failed to execute."
    exit 1
fi

# accessiondata= curl -X GET "https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/human/dataset_report" \
# -H 'accept: application/json' | jq

# echo $accessiondata.reports.taxonomy
# for thing in "${accessions[@]}"; do
#     echo $thing
# done