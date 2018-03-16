#!/usr/bin/env python3
# By Liam McKay (ltmckay) and Paola Angulo (pangulo)
# polyAriboDclassifier-v2.py



####################################################################################
# MAIN PROGRAM
# 
# Finds the method of preparation for the transcriptome from a sequence partner 
# in the Treehouse Initiative 
# Usage: $ python polyAriboDclassifier-v2.py [-nG [--noGene]] inputFile.tsv outputFile
####################################################################################


import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import sys
########################################################################
# CommandLine
########################################################################
class CommandLine() :
	'''
	Handle the command line, usage and help requests.

	CommandLine uses argparse, now standard in 2.7 and beyond. 
	it implements a standard command line argument parser with various argument options,
	a standard usage and help.

	attributes:
	all arguments received from the commandline using .add_argument will be
	avalable within the .args attribute of object instantiated from CommandLine.
	For example, if myCommandLine is an object of the class, and requiredbool was
	set as an option using add_argument, then myCommandLine.args.requiredbool will
	name that option.
 
	'''
	
	def __init__(self, inOpts=None) :
		'''
		Implement a parser to interpret the command line argv string using argparse.
		'''
		
		import argparse
		self.parser = argparse.ArgumentParser(description = 'Find the method of sequencing of a gene expression column', 
											 epilog = 'Uses 95th pctl, variance, mean calculation of new and old reference samples', 
											 add_help = True, #default is True 
											 prefix_chars = '-', 
											 usage = '%(prog)s [options] -option1[default] <input >output'
											 )
		self.parser.add_argument('inFile', action = 'store', help='input file name')
		self.parser.add_argument('outFile', action = 'store', help='output file name') 
		self.parser.add_argument('-nG', '--noGene', action = 'store', nargs='?', const=True, default=False, help='Use this flag if there is no Gene column')
		self.parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')  
		if inOpts is None :
			self.args = self.parser.parse_args()
		else :
			self.args = self.parser.parse_args(inOpts)

def main(inCL=None):
	'''
	Find PolyA-Selection or Ribo-Depletion of a column of gene expression data by 
	comparing the 95th percentile, variance, and mean of a reference set to the new
	sample.
	Command Line arguments: 
	-nG --noGene: use if your new sample does not have a "Gene" column, otherwise 
				  the program assumes that there is a Gene column and removes it.

	'''
	if inCL is None:
		myCommandLine = CommandLine()
	else :
		myCommandLine = CommandLine(inCL)


	# open file for output
	inputFile = myCommandLine.args.inFile 
	outputFile = myCommandLine.args.outFile 
	outputFileObject = open(outputFile, 'w')
	newSampdf = pd.read_csv(inputFile, sep="\t")

	# ------------------------------------------------
	# classification calculations:

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

	# drop gene column in the new sample's dataframe
	if(myCommandLine.args.noGene == False):
		newSampdf = newSampdf.drop("Gene", axis=1)


	for col in newSampdf.columns :
		threeValsNewSamp = np.array([newSampPctlDf[col],newSampVarianceDf[col],newSampMeanDf[col]])
		differenceToRiboD = np.subtract(threeValsNewSamp, threeValsRiboD)
		differenceToPolyA = np.subtract(threeValsNewSamp, threeValsPolyA)
		
		# scoring method based on how close each p95, var, mean is to the respective reference method
		riboDScore = 0
		polyAScore = 0
		for i in range(0,3):
			if (abs(differenceToPolyA[i])<abs(differenceToRiboD[i])):
				polyAScore+=1
			else:
				riboDScore+=1
		if(riboDScore>polyAScore):
			outputFileObject.write("{0}\tRiboMinus\n".format(col))
		else:
			outputFileObject.write("{0}\tPolyA\n".format(col))

	
if __name__ == "__main__":
	main() 

