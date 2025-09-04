from Bio import Entrez, SeqIO


Entrez.email = "kmdavidson1@wpi.edu"

# Searches NCBI for search term and downloads fasta sequences
search_term = "txid694002[Organism:exp] AND srcdb_refseq[PROP]"  # restrict to RefSeq proteins this is second term
handle = Entrez.esearch(db="protein", term=search_term, retmax=100000)

record = Entrez.read(handle)
handle.close()

id_list = record["IdList"]
print(f"Found {len(id_list)} protein sequences.")


if id_list:
    batch_size = 500
    with open("data/sequences/betacoronavirus_proteins.fasta", "w") as out_f:
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
