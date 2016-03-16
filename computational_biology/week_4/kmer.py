from __future__ import division
from operator import itemgetter
import sys, re, csv

def read_sequence(fin):
	dna_file = open(fin)
	dna = csv.reader(dna_file, delimiter='\n')
	return dna 

def kmer(dna):
 	sequences_list = []
 	for line in dna:
		sequences_list.append(line)


	for x in sequences_list:
		kmers = []
		n = sequences_list[x]
	print n

	
	# for i in range(0, n-k+1):
	# 	kmers.append(sequences_list[i:i+k])
	# print kmers



def main(dna):
	dnas = read_sequence(dna)
	kmer(dnas)

	

if __name__ == "__main__":
    main(sys.argv[1]) 