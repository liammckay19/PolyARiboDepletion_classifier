# Code to wrangle the data in python
# Liam McKay (ltmckay) and Paola Angulo (pangulo)
# dontRunMeInPython_getPublicSampleDataFrame_runMeByEachLine.py 

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



#Boxplots of data:
mpl.use('agg')
fig = plt.figure()
ax = fig.add_subplot(111)
bp = plt.boxplot((polyAMeanDf,riboDMeanDf))
ax.set_title('Mean Across Each PolyA and RiboD Sequenced Sample: PolyA Mean vs.log2 (TPM+1)')
ax.set_xticklabels(['polyA','riboD'])
ax.set_ylabel('log2 (TPM+1)')
plt.show()
fig.savefig('fig1_Means.png')

bp2 = plt.boxplot((polyAVarDf,riboDVarDf))
ax.set_title('Variance Across Each PolyA and RiboD Sequenced Sample: PolyA Var vs.log2 (TPM+1)')
ax.set_xticklabels(['polyA','riboD'])
ax.set_ylabel('log2 (TPM+1)')
plt.show()
fig.savefig('fig2_Var.png')

bp3 = plt.boxplot((polyAPtclDf,riboDPtclDf))
ax.set_title('95th Percentile Across Each PolyA and RiboD Sequenced Sample: PolyA 95p vs.log2 (TPM+1)')
ax.set_xticklabels(['polyA','riboD'])
ax.set_ylabel('log2 (TPM+1)')
plt.show()
fig.savefig('fig2_95P.png')
