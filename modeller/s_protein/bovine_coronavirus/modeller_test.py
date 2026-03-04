from modeller import *
from modeller.automodel import *

# A nice PDB file here 7ZH1 for Sars_COV_1 spike protein

log.verbose()
env = Environ()
mdl = Model(env, file="./6VXX.pdb", model_format='PDB_OR_MMCIF')
mdl2 = Model(env, file="./bovine_coronavirus_s_protein.pdb", model_format='PDB_OR_MMCIF')
aln = Alignment(env)
aln.append_model(mdl, align_codes="6VXX")
aln.append_model(mdl2, align_codes="bcovsp")

# aln.append(file="./s_protein_sars_cov_1.seq", align_codes=f"sars_cov_1")
aln.salign()
aln.write(file="./6VXX_bcovsp.ali")

a = AutoModel(env, alnfile="./6VXX_bcovsp.ali", knowns="6VXX", sequence="bcovsp", inifile="bovine_coronavirus_s_protein.pdb")
a.starting_model = 1
a.ending_model = 1
a.make()