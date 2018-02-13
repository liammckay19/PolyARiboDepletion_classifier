#!/usr/bin/env python3
# Name: Paola Angulo (pangulo)
# Group Members: Will Lewczk (wlewczk)
'''
Takes a string of amino acids and counts the amino acids, returns the molecular weight, the molar/mass extinction coefficient,
theoretical pI, and the amino acid composition.

Example: 
 input: VLSPADKTNVKAAW
 output: 
Number of Amino Acids: 14
Molecular Weight: 1499.7
molar Extinction coefficient: 5500.00
mass Extinction coefficient: 3.67
Theoretical pI: 9.88
Amino acid composition:
A = 21.43%
C = 0.00%
D = 7.14%
E = 0.00%
F = 0.00%
G = 0.00%
H = 0.00%
I = 0.00%
K = 14.29%
L = 7.14%
M = 0.00%
N = 7.14%
P = 7.14%
Q = 0.00%
R = 0.00%
S = 7.14%
T = 7.14%
V = 14.29%
W = 7.14%
Y = 0.00%
 
'''

class ProteinParam :
# These tables are for calculating:
#     molecular weight (aa2mw), along with the mol. weight of H2O (mwH2O)
#     absorbance at 280 nm (aa2abs280)
#     pKa of positively charged Amino Acids (aa2chargePos)
#     pKa of negatively charged Amino acids (aa2chargeNeg)
#     and the constants aaNterm and aaCterm for pKa of the respective termini
#  Feel free to move these to appropriate methods as you like

# As written, these are accessed as class attributes, for example:
# ProteinParam.aa2mw['A'] or ProteinParam.mwH2O
    aa2mw = {
        'A': 89.093,  'G': 75.067,  'M': 149.211, 'S': 105.093, 'C': 121.158,
        'H': 155.155, 'N': 132.118, 'T': 119.119, 'D': 133.103, 'I': 131.173,
        'P': 115.131, 'V': 117.146, 'E': 147.129, 'K': 146.188, 'Q': 146.145,
        'W': 204.225,  'F': 165.189, 'L': 131.173, 'R': 174.201, 'Y': 181.189
        }
    mwH2O = 18.015
    
    aa2chargePos = {'K': 10.5, 'R':12.4, 'H':6}
    aa2chargeNeg = {'D': -3.86, 'E': -4.25, 'C': -8.33, 'Y': -10}
    aaNterm = 9.69
    aaCterm = 2.34 
    
    aa2abs280= {'Y':1490, 'W': 5500, 'C': 125}
    
    def __init__ (self, protein):
        
        self.protein = protein.upper()
        #Turns user input string into all caps
       
        self.aaName = {
            'A': 0,  'G': 0,  'M': 0, 'S': 0, 'C': 0,
            'H': 0, 'N': 0, 'T': 0, 'D': 0, 'I': 0,
            'P': 0, 'V': 0, 'E': 0, 'K': 0, 'Q': 0,
            'W': 0,  'F': 0, 'L': 0, 'R': 0, 'Y': 0
            } 
        #put aaComposition dictionary in here to only return it in method aaComposition
        
        for aa in self.protein:
            if aa in self.aaName:
                self.aaName[aa] += 1
        #this will count each amino acid in the protein sequence
        
    def aaCount (self):
        """counts total amino acids in the sequence"""
    
        count = 0
        for aa in self.protein:
            if aa in self.aa2mw:
                count += 1
        return (count)

    def pI (self):
        """iterates through each pH while calling on _charge_() method and returns the best pH that is has a charge closest 
        to zero"""
    
        bestCharge = 10000000
        for pH in range(1400+1):
            totalCharge = self._charge_(pH/100)
            if bestCharge > abs(totalCharge) :
                bestCharge = abs(totalCharge) 
                bestPh = pH/100
        return(bestPh)


    def aaComposition (self) :
        return(self.aaName)

    def _charge_ (self, pH):
        """uses the formula to get net charge for each amino acid in the protein sequence"""
        
        nposCharge = (10**self.aaNterm)/((10**self.aaNterm)+(10**pH))
        
        nnegCharge = (10**pH)/((10**self.aaCterm)+(10**pH))
        #these two cannot be in the for loop because they should only be added once, so they can be added after the calculation 
        #of each of the amino acids that have a charge
        
        newChargepos = 0 
        newChargeneg = 0
        
        for aa in self.aaName:
            if aa in self.aa2chargePos:
                chargePos = self.aaName[aa]*((10**self.aa2chargePos[aa])/((10**self.aa2chargePos[aa])+(10**pH)))
                newChargepos += chargePos
        newChargepos += nposCharge
        #by using a for loop each amino acid that has a positive charge can be added together using the same formula        
        
        for aa in self.aaName:  
            if aa in self.aa2chargeNeg:
                chargeNeg = self.aaName[aa]*((10**pH)/((10**self.aa2chargeNeg[aa])+(10**pH)))
                newChargeneg += chargeNeg
        newChargeneg += nnegCharge 
        #by using a for loop each amino acid that has a positive charge can be added together using the same formula
        
        netCharge = newChargepos - newChargeneg
        return(netCharge)     

    def molarExtinction (self):
        """Uses a simple formula in a for loop to add together the extinction coefficient of each amino acid in the sequence"""
    
        totalExt = 0
        for aa in self.aaName:
            if aa in self.aa2abs280:
                ext = self.aaName[aa]*self.aa2abs280[aa]
                totalExt += ext
        return(totalExt)

    def massExtinction (self):
        myMW =  self.molecularWeight()
        return self.molarExtinction() / myMW if myMW else 0.0

    def molecularWeight (self):
        """Uses a simple formula in a for loop to add together the molecular weight of each amino acid in the sequence along with
        the molecular weight of each water molecule that is added to the amino acid sequence"""
        
        total_mw = self.mwH2O
        for aa in self.aa2mw:
            if aa in self.aa2mw:
                mw  = self.aaName[aa] * (self.aa2mw[aa] - self.mwH2O)
                total_mw += mw #adds molecular weight of water each time
        return(total_mw)
        
        

# Please do not modify any of the following.  This will produce a standard output that can be parsed
    
import sys
def main():
    inString = input('protein sequence?')
    while inString :
        myParamMaker = ProteinParam(inString)
        myAAnumber = myParamMaker.aaCount()
        print ("Number of Amino Acids: {aaNum}".format(aaNum = myAAnumber))
        print ("Molecular Weight: {:.1f}".format(myParamMaker.molecularWeight()))
        print ("molar Extinction coefficient: {:.2f}".format(myParamMaker.molarExtinction()))
        print ("mass Extinction coefficient: {:.2f}".format(myParamMaker.massExtinction()))
        print ("Theoretical pI: {:.2f}".format(myParamMaker.pI()))
        print ("Amino acid composition:")
        myAAcomposition = myParamMaker.aaComposition()
        keys = list(myAAcomposition.keys())
        keys.sort()
        if myAAnumber == 0 : 
            myAAnumber = 1  # handles the case where no AA are present 
        for key in keys :
            print ("\t{} = {:.2%}".format(key, myAAcomposition[key]/myAAnumber))
            
        inString = input('protein sequence?')

if __name__ == "__main__":
    main()