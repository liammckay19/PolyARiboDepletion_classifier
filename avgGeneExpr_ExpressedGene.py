# - plot avg gene expression vs. expressed genes scatter plot (liam)
# avgGeneExpr_ExpressedGene.py (liam’s)

import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

fname = 'treehouse_public_samples_unique_hugo_log2_tpm_plus_1.2017-09-11.tsv'
print(fname)

# TARGET-51
# THR21
# TH01
# these are ribominus

# reading data and initial calculations: 
polyA = [c for c in data.columns if c[:4] != 'TH01']
df1=data[polyA]
polyA = [c for c in df1.columns if c[:5] != 'THR21']
df2=df1[polyA]
polyA = [c for c in df2.columns if c[:9] != 'TARGET-51']
polyAdf=df2[polyA]


polyAVarianceDf = polyAdf.var(axis=0)
polyAMeanDf = polyAdf.mean(axis=0)
polyAPctlDf = polyAdf.quantile(0.95)
polyAVarianceDf.to_pickle('polyAVarDf.pkl')
polyAMeanDf.to_pickle('polyAMeanDf.pkl')
polyAPctlDf.to_pickle('polyAPtclDf.pkl')

suspectedRiboD = ("TH01_0051_S01","TH01_0053_S01","TH01_0054_S01","TH01_0055_S01","TH01_0061_S01","TH01_0062_S01","TH01_0063_S01","TH01_0064_S01","TH01_0069_S01")

riboD = [c for c in data.columns if (c[:5] == 'THR21' or c[:9] == 'TARGET-51' or c[:4] == 'TH01') and c[:13] not in suspectedRiboD]
riboDdf=data[riboD]

riboDVarianceDf = riboDdf.var(axis=0)
riboDMeanDf = riboDdf.mean(axis=0)
riboDPctlDf = riboDdf.quantile(0.95)
riboDVarianceDf.to_pickle('riboDVarDf.pkl')
riboDMeanDf.to_pickle('riboDMeanDf.pkl')
riboDPctlDf.to_pickle('riboDPtclDf.pkl')



# distance calculations:
riboDp95 = riboDPctlDf.mean(axis=0)
riboDVar = riboDVarianceDf.mean(axis=0)
riboDMean = riboDMeanDf.mean(axis=0)

polyAp95 = polyAPctlDf.mean(axis=0)
polyAVar = polyAVarianceDf.mean(axis=0)
polyAMean = polyAMeanDf.mean(axis=0)

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


polyAVarianceDf = pd.read_pickle('polyAVarDf.pkl')
polyAMeanDf = pd.read_pickle('polyAMeanDf.pkl')
polyAPctlDf = pd.read_pickle('polyAPtclDf.pkl')
#plot data
plt.boxplot((polyAPctlDf, polyAVarianceDf, polyAMeanDf))
#labels
plt.xlabel("this is X")
plt.ylabel("this is Y")
#title
plt.title("PolyA p95, Variance, Mean")
#show plot
plt.show()

riboDVarianceDf = pd.read_pickle('riboDVarDf.pkl')
riboDMeanDf = pd.read_pickle('riboDMeanDf.pkl')
riboDPctlDf = pd.read_pickle('riboDPtclDf.pkl')

# Distance calculation of mean
threeValsRiboD = np.array([riboDp95[0],riboDVar[0],riboDMean[0]])
# figure out how to access mean value in dataframes of one value

threeValsPolyA = np.array([polyAp95[0],polyAVar[0],polyAMean[0]])


# new sample
# newSampVarianceDf = newSampdf.var(axis=0)
# newSampMeanDf = newSampdf.mean(axis=0)
# newSampPctlDf = newSampdf.quantile(0.95)
# newSampVarianceDf.to_pickle('newSampVarDf.pkl')
# newSampMeanDf.to_pickle('newSampMeanDf.pkl')
# newSampPctlDf.to_pickle('newSampPtclDf.pkl')

# for col in newSampPctlDf.columns :
# 	threeValsNewSamp = np.array([newSampPctlDf[col],newSampVarianceDf[col],newSampMeanDf[col]])
# 	differenceToRiboD = np.subtract(threeValsNewSamp, threeValsRiboD)
# 	differenceToRiboD = np.absolute(differenceToRiboD)
# 	differenceToPolyA = np.subtract(threeValsNewSamp, threeValsPolyA)
# 	differenceToPolyA = np.absolute(differenceToPolyA)

# 	if(differenceToPolyA > differenceToRiboD):
# 		print("{0}\tRiboD".format(col))
# 	elif(differenceToPolyA < differenceToRiboD):
# 		print("{0}\tPolyA".format(col))


# # x,y = np.loadtxt(fname, delimiter='\t', unpack=True)
# # print(x,y)
# # print(sampleValues)
# # print(x)
# # x = np.loadtxt('treehouse_public_samples_unique_hugo_log2_tpm_plus_1.2017-09-11.tsv', delimiter='\t', unpack=True, skiprows = 62742)
# zeroCount = [i for i, e in enumerate(sampleValues) if e != 0]
# plt.hist(zeroCount)

if __name__ == "__main__":
	main()  # delete the list when you want to run normally
