from __future__ import division
from Bio import SearchIO
import re
import sys

def readblast(blast):
	blast_file = open(blast)
	blast = blast_file.read()
	query_subject = '' #create an empty dict to get rid of duplicates 
	for line in blast:
		if not line.startswith('#'): #skip the first line of fasta file
			query_subject += line.split('|')
	print query_subject #append the sequence to empty string, strips any underwanted spaces, makes all uppercase incase of lowercase seq elements
	
	

#def seq_dict(file):

def main(file):
	blast = readblast(sys.argv[1])
	print blast
if __name__ == "__main__":
    main(sys.argv[1])