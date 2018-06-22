# PolyARiboDClassifier
Undergraduate research by Liam McKay mentored by Holly Beale. 
Thanks to the whole Treehouse team: 


# What This Does<br>
<br>
Creates data sets for training and testing a Logistic Regression model to classify Ribosomal RNA depletion and Polyadenylation Selection methods from gene expression values in log2(TPM+1)<br>
DESeq analysis on the compendium within subtypes of disease that (future) is to be used to create differentially expressed features<br>

# Dependencies
Install Anacaonda for python 3: https://anaconda.org/anaconda/python<br>
(To check what version of python you have type python --version)<br>
Run dependenciesPython and dependenciesR notebooks to see if all dependencies are installed<br>

# Quickstart:
- load dependenciesPython and dependenciesR hopefully without error
- run datasiftingfinal notebook to gather data in data/ folder in this directory
- run trainingGliomaAllGenes and trainingGliomaHighVar to see Logistic Regression model testing
- run DESeqGenes to get genes that are differentially expressed between polyA and riboD within a disease
