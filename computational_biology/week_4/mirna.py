from __future__ import division
from operator import itemgetter
import sys, re, csv


#make both files into one big file ... wanted to try this out.
reads = ['/data/mirna/read1.txt', '/data/mirna/read2.txt'] 
with open('read_comp.txt', 'w') as fout: 
	for i in reads:
		with open(i) as fin:
			for k in fin:
				fout.write(k)

read_comp = 'read_comp.txt'
open_read = open(read_comp)
print_read = open_read.read().strip()	

with open('read_comp.txt') as read_raw, open('/data/mirna/targets.tsv') as target_file:
	reads = csv.reader(read_raw, delimiter='\t') #use the csv reader to delimit by new line as well
	targetfile = csv.reader(target_file, delimiter='\t')

	target_seq = [] #create an empty list of the miRNA search term sequences
	data = []
	for line in targetfile:
		targets = line[5] #targets are the 6th element 
		target_seq.append(targets) #append the target after each iteration through the for loop
		data.append(line)

	
	read_seq = [] #creates an empty list of the sequences from the read file 
	for line in reads: 
		read_seq.append(line) 

	mirna = []
	counts = []
	for search in target_seq: #for loop through a for loop to iterate the search term list through the target list 
		readcounter = 0	
		totalread = 0	
		for sequences in read_seq:	
			totalread += int(sequences[1]) #append total read for normalization calc
			if re.search(search, str(sequences)): #re.search - argument 1 = search term; argument 2 = what you're searching through
				readcounter += int(sequences[1])
				continue
			else:
				continue
		if readcounter > 0: #if the read has more the one count ... start collecting the matched seq in [mirna] and number of matched in [counts]
			mirna.append(search)
			counts.append(readcounter)

	normalized_counts = []
	for line in counts:
		counter = line / totalread
		normalized_counts.append(counter)

	gene_ids = [] 
	mirna_list = []
	for line in mirna:
		for lines in data:
			if re.search(line, str(lines)):
				genes = lines[0]
				gene_ids.append(genes)
				names = lines[1]
				mirna_list.append(names)
			else:
				continue

	#have all of the info that is needed, now sort the files by element location such that it is in descending order of count
	final = [(mirna_list[i],gene_ids[i],counts[i],normalized_counts[i]) for i in range(len(normalized_counts))]
	print sorted(final, key=itemgetter(2), reverse=True)



	