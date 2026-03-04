from modeller import *
from modeller.automodel import *

# A nice PDB file here 7ZH1 for Sars_COV_1 spike protein

log.verbose()
env = Environ()
mdl = Model(env, file="./flabE.pdb", model_format='PDB_OR_MMCIF')
mdl2 = Model(env, file="./murine_coronavirus_e_protein.pdb", model_format='PDB_OR_MMCIF')
aln = Alignment(env)
aln.append_model(mdl, align_codes="flabE")
aln.append_model(mdl2, align_codes="mcep")

# aln.append(file="./s_protein_sars_cov_1.seq", align_codes=f"sars_cov_1")
aln.salign()
aln.write(file="./flabE_mcep.ali")
a = AutoModel(env, alnfile="./flabE_mcep.ali", knowns="flabE", sequence="mcep", inifile="murine_coronavirus_e_protein.pdb")
a.starting_model = 1
a.ending_model = 1
a.make()