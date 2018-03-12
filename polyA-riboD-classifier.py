# riboD-polyA-classifier.py


import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd


def main():
	inputFileName = sys.stdin
	newSample = pd.read_csv(inputFileName, sep="\t")
	data = pd.read_csv(fname, sep="\t")

	# distance calculations:

	# Load these in from values returned by avgGeneExpr_ExpressedGene.py
	riboDp95 = 0
	riboDVar = 4
	riboDMean = 3
	polyAp95 = 1
	polyAVar = 5
	polyAMean = 9

	# Distance calculation of mean
	threeValsRiboD = np.array([riboDp95,riboDVar,riboDMean])
	# figure out how to access mean value in dataframes of one value

	threeValsPolyA = np.array([polyAp95,polyAVar,polyAMean])


	# new sample
	newSampVarianceDf = newSampdf.var(axis=0)
	newSampMeanDf = newSampdf.mean(axis=0)
	newSampPctlDf = newSampdf.quantile(0.95)

	for col in newSampPctlDf.columns :
		threeValsNewSamp = np.array([newSampPctlDf[col],newSampVarianceDf[col],newSampMeanDf[col]])
		differenceToRiboD = np.subtract(threeValsNewSamp, threeValsRiboD)
		differenceToRiboD = np.absolute(differenceToRiboD)
		differenceToPolyA = np.subtract(threeValsNewSamp, threeValsPolyA)
		differenceToPolyA = np.absolute(differenceToPolyA)

		if(differenceToPolyA > differenceToRiboD):
			print("{0}\tRiboD".format(col))
		elif(differenceToPolyA < differenceToRiboD):
			print("{0}\tPolyA".format(col))

