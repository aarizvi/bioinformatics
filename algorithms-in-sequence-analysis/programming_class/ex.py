with open('/data/dna/genomic_dna.txt') as fin, open('output.txt', 'w') as fout:
	for i in fin:
		dna = i[14:]
		print 'length seq:', len(dna)