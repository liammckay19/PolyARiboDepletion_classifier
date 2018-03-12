# riboD-polyA-classifier.py


import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import sys

def main():

	inputFileName = sys.stdin
	newSampdf = pd.read_csv(inputFileName, sep="\t")
	print(newSampdf)	

# # >>> polyAp95
# 5.340720200699123
# >>> polyAVar
# 3.649240487654772
# >>> polyAMean
# 1.0491995456139986


# >>> riboDp95
# 3.6812559832605625
# >>> riboDVar
# 1.881014066540907
# >>> riboDMean
# 0.7170628642305512

	# distance calculations:

	# Load these in from values returned by avgGeneExpr_ExpressedGene.py
	riboDp95 = 3.6812559832605625
	riboDVar = 1.881014066540907
	riboDMean = 0.7170628642305512
	polyAp95 = 5.340720200699123
	polyAVar = 3.649240487654772
	polyAMean = 1.0491995456139986

	# Distance calculation of mean
	threeValsRiboD = np.array([riboDp95,riboDVar,riboDMean])
	# figure out how to access mean value in dataframes of one value

	threeValsPolyA = np.array([polyAp95,polyAVar,polyAMean])


	# new sample
	newSampVarianceDf = newSampdf.var(axis=0)
	newSampMeanDf = newSampdf.mean(axis=0)
	newSampPctlDf = newSampdf.quantile(0.95)

	newSampdf = newSampdf.drop("Gene", axis=1)

	for col in newSampdf.columns :
		threeValsNewSamp = np.array([newSampPctlDf[col],newSampVarianceDf[col],newSampMeanDf[col]])
		differenceToRiboD = np.subtract(threeValsNewSamp, threeValsRiboD)
		differenceToRiboD = np.absolute(differenceToRiboD).sum()
		differenceToPolyA = np.subtract(threeValsNewSamp, threeValsPolyA)
		differenceToPolyA = np.absolute(differenceToPolyA).sum()
		print(threeValsNewSamp)

		print("polya", differenceToPolyA)
		print("ribod", differenceToRiboD)

		if(differenceToPolyA > differenceToRiboD):
			print("{0}\tRiboD".format(col))
		elif(differenceToPolyA < differenceToRiboD):
			print("{0}\tPolyA".format(col))

main()