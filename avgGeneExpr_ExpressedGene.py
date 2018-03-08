# - plot avg gene expression vs. expressed genes scatter plot (liam)
# avgGeneExpr_ExpressedGene.py (liam’s)

import matplotlib.pyplot as plt
import csv
import numpy as np
import os
import pandas as pd
def main():


	i = 1

	# sampleValues = [[],[]]
	# with open('treehouse_public_samples_unique_hugo_log2_tpm_plus_1.2017-09-11.tsv') as tsvfile:
	# 	reader = csv.reader(tsvfile, delimiter='\t')
	# 	for col in reader :
	# 		sampleValues.append(col)
	fname = 'treehouse_public_samples_unique_hugo_log2_tpm_plus_1.2017-09-11.tsv'
	print(fname)


	data = pd.read_csv(fname, sep="\t", header=None)



	# x,y = np.loadtxt(fname, delimiter='\t', unpack=True)
	# print(x,y)
	# print(sampleValues)
	# print(x)
	# x = np.loadtxt('treehouse_public_samples_unique_hugo_log2_tpm_plus_1.2017-09-11.tsv', delimiter='\t', unpack=True, skiprows = 62742)
	zeroCount = [i for i, e in enumerate(sampleValues) if e != 0]
	plt.hist(zeroCount)

if __name__ == "__main__":
	main()  # delete the list when you want to run normally
