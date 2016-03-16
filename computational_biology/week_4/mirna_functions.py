#homework 3
#question 1 -- find which miRNA has the potential for binding and which gene it regulates

#read1 - raw sequencing reads (tags)
#read2 - corresponding counts 

import re
import sys
import csv

#reads = ['read1.txt', 'read2.txt']

# with open('/Users/aarizvi/Desktop/ROSWELL_MS/week_4/read_comp.txt', 'w') as fout: 
# 	for i in reads:
# 		with open(i) as fin:
# 			for k in fin:
# 				fout.write(k)

# read_comp = 'read_comp.txt'
# open_read = open(read_comp)
# print_read = open_read.read().strip().splitlines()

#open target.tsv
def read_targets(fin):
	target_file = open(fin)
	targetread = csv.reader(target_file, delimiter='\t')
	return targetread 

#open compiled read file
# def open_read(readfile):
# 	read_raw = open(readfile)
# 	reads = csv.reader(read_raw, delimiter='\t')
# 	return reads

def seq_list(targetread, reads):
	sequences_list = []
	for line in targetread:
		targets = line[5]
		#print targets
		sequences_list.append(targets)
		for k in reads:
			seq = k[0]

	return sequences_list

def names_list(targetread):
	names_list = []
	for line in targetread:
		names = line[0]
		#print targets
		names_list.append(names)
	return names_list

def mirna_list(targetread):
	mirna_list = []
	for line in targetread:
		mirna = line[1]
		#print mirna 
		mirna_list.append(mirna)
	return mirna_list 


def read_lists(fin):
	read_raw = open(fin)
	reads = csv.reader(read_raw, delimiter='\t')
	return reads

def fuckyou(reads):
	read_seq = []
	for k in reads:
		seq = k[0]
		count = k[1]
		read_seq.append(seq)
	return read_seq

def matches(target, targetread, readfile):
	for mirna in targetread:
		print 'kkkkk',mirna
		for matches in readfile:
			print 'fuck',matches


def main(targetread, reads):
	target = read_targets(targetread)

	read = read_lists(reads)
	print seq_list(target, read)
	sequences = seq_list(target, read)
	target = read_targets(targetread)
	print names_list(target)

	target = read_targets(targetread)
	print mirna_list(target)

	read = read_lists(reads)
	print fuckyou(read)

	targetread = read_targets(targetread)

	print matches(target, sequences, read)
	


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

