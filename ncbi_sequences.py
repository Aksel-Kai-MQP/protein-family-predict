from Bio import Entrez, SeqIO

Entrez.email = ""

# Sars-CoV-1 txid694009
# Sars-CoV-2 txid2697049
# MERS-CoV txid1335626
# Murine Coronavirus MHV txid694005
# Bovine Coronavirus BCoV txid11128
# Bat Coronavirus txid
# Human Coronavirus HCoV-HKU1 txid290028

species = [
    {"name": "Sars-CoV-1", "tax_id": "txid694009[Organism:exp]"},  # Sars-Cov-1
    {"name": "Sars-CoV-2", "tax_id": "txid290028[Organism:exp]"},  # HCoV
    {"name": "Murine Coronavirus MHV", "tax_id": "txid694005[Organism:exp]"},  # Murine
    {"name": "MERS-CoV", "tax_id": "txid1335626[Organism:exp]"},  # MERS
    {"name": "Bovine Coronavirus BCoV", "tax_id": "txid11128[Organism:exp]"},  # Bovine
    # "txid2697049[Organism:exp]", Sars-cov-2
]

# Searches NCBI for search term and downloads fasta sequences
for entry in species:
    search_term = f"{entry["tax_id"]} AND srcdb_refseq[PROP]"  # restrict to RefSeq proteins this is second term
    handle = Entrez.esearch(db="protein", term=search_term, retmax=100000)

    record = Entrez.read(handle)
    handle.close()

    id_list = record["IdList"]
    print(f"Found {len(id_list)} protein sequences.")

    if id_list:
        batch_size = 500
        with open(f"data/sequences/{entry["name"]}.fasta", "w") as out_f:
            for start in range(0, len(id_list), batch_size):
                end = min(len(id_list), start + batch_size)
                fetch_ids = id_list[start:end]
                fetch_handle = Entrez.efetch(
                    db="protein", id=fetch_ids, rettype="fasta", retmode="text"
                )
                data = fetch_handle.read()
                fetch_handle.close()
                out_f.write(data)
                print(f"Downloaded {start+1}-{end} of {len(id_list)}")
