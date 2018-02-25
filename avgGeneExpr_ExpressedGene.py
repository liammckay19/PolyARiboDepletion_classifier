# - plot avg gene expression vs. expressed genes scatter plot (liam)
# avgGeneExpr_ExpressedGene.py (liam’s)

import csv
		

def main():


	with open('treehouse_public_samples_unique_hugo_log2_tpm_plus_1.2017-09-11.tsv','rb') as tsvin, open('new.csv', 'wb') as csvout:
	    tsvin = csv.reader(tsvin, delimiter='\t')
	    csvout = csv.writer(csvout)

	    for row in tsvin:
	        count = int(row[4])
	        if count > 0:
	            csvout.writerows([row[2:4] for _ in xrange(count)])



if __name__ == "__main__":
	main()  # delete the list when you want to run normally
