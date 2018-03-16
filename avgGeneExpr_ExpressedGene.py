# - plot avg gene expression vs. expressed genes scatter plot
# avgGeneExpr_ExpressedGene.py 

import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

# run python within the file containing this tsv file
fname = 'treehouse_public_samples_unique_hugo_log2_tpm_plus_1.2017-09-11.tsv'
print(fname)
ckccPubSamples = pd.read_csv(fname, sep="\t")
# loads data


# TARGET-51
# THR21
# TH01
# these are ribominus

## reading data and initial calculations: 

# find all PolyA selected Samples from reference set (TranscriptMethod_THPEDv1.csv)
polyA = [c for c in ckccPubSamples.columns if c[:4] != 'TH01']
df1=ckccPubSamples[polyA]
polyA = [c for c in df1.columns if c[:5] != 'THR21']
df2=df1[polyA]
polyA = [c for c in df2.columns if c[:9] != 'TARGET-51']
polyAdf=df2[polyA]
# stores dataframe of all polyA samples to be read later
polyAdf.to_pickle('polyAdf.pkl')

# attempt to calculate mean of all polyA samples
polyAdf['mean'] = polyAdf.mean(axis=1)

# current way of getting 95th percentile, variance and mean for polyA
polyAVarianceDf = polyAdf.var(axis=0)
polyAMeanDf = polyAdf.mean(axis=0)
polyAPctlDf = polyAdf.quantile(0.95)
polyAVarianceDf.to_pickle('polyAVarDf.pkl')
polyAMeanDf.to_pickle('polyAMeanDf.pkl')
polyAPctlDf.to_pickle('polyAPtclDf.pkl')

# gather all riboD samples into a dataframe
suspectedRiboD = ("TH01_0051_S01","TH01_0053_S01","TH01_0054_S01","TH01_0055_S01","TH01_0061_S01","TH01_0062_S01","TH01_0063_S01","TH01_0064_S01","TH01_0069_S01")
riboD = [c for c in data.columns if (c[:5] == 'THR21' or c[:9] == 'TARGET-51' or c[:4] == 'TH01') and c[:13] not in suspectedRiboD]
riboDdf=data[riboD]

# current way of getting 95th percentile, variance and mean for polyA
riboDVarianceDf = riboDdf.var(axis=0)
riboDMeanDf = riboDdf.mean(axis=0)
riboDPctlDf = riboDdf.quantile(0.95)
riboDVarianceDf.to_pickle('riboDVarDf.pkl')
riboDMeanDf.to_pickle('riboDMeanDf.pkl')
riboDPctlDf.to_pickle('riboDPtclDf.pkl')



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


# read data from previously stored data
polyAVarianceDf = pd.read_pickle('polyAVarDf.pkl')
polyAMeanDf = pd.read_pickle('polyAMeanDf.pkl')
polyAPctlDf = pd.read_pickle('polyAPtclDf.pkl')
# plot data
plt.boxplot((polyAPctlDf, polyAVarianceDf, polyAMeanDf))
# labels
plt.xlabel("this is X")
plt.ylabel("this is Y")
# title
plt.title("PolyA p95, Variance, Mean")
# show plot
plt.show()

riboDVarianceDf = pd.read_pickle('riboDVarDf.pkl')
riboDMeanDf = pd.read_pickle('riboDMeanDf.pkl')
riboDPctlDf = pd.read_pickle('riboDPtclDf.pkl')

# Distance calculation of mean
threeValsRiboD = np.array([riboDp95[0],riboDVar[0],riboDMean[0]])

# figure out how to access mean value in dataframes of one value
threeValsPolyA = np.array([polyAp95[0],polyAVar[0],polyAMean[0]])


if __name__ == "__main__":
	main()  # delete the list when you want to run normally
