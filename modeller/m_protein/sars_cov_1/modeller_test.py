from modeller import *
from modeller.automodel import *

# A nice PDB file here 7ZH1 for Sars_COV_1 spike protein

log.verbose()
env = Environ()
mdl = Model(env, file="./flabM.pdb", model_format='PDB_OR_MMCIF')
mdl2 = Model(env, file="./sars_cov_1_m_protein.pdb", model_format='PDB_OR_MMCIF')
aln = Alignment(env)
aln.append_model(mdl, align_codes="flabM")
aln.append_model(mdl2, align_codes="sc1mp")

# aln.append(file="./s_protein_sars_cov_1.seq", align_codes=f"sars_cov_1")
aln.salign()
aln.write(file="./flabM_sc1mp.ali")
a = AutoModel(env, alnfile="./flabM_sc1mp.ali", knowns="flabM", sequence="sc1mp", inifile="sars_cov_1_m_protein.pdb")
a.starting_model = 1
a.ending_model = 1
a.make()