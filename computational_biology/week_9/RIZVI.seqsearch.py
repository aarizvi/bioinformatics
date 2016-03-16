import sys
import re

nt_code = {
 "A" : "A",
 "T" : "T",
 "C" : "C",
 "G" : "G",
 "R" : "[AG]",
 "Y" : "[CT]",
 "S" : "[GC]",
 "W" : "[AT]",
 "K" : "[GT]",
 "M" : "[AC]",
 "B" : "[CGT]",
 "D" : "[AGT]",
 "H" : "[ACT]",
 "V" : "[ACG]",
 "N" : "[ATCG]"
}

rev_nt_code = {
 "A" : "T",
 "T" : "A",
 "C" : "G",
 "G" : "C",
 "R" : "[TC]",
 "Y" : "[GA]",
 "S" : "[GC]",
 "W" : "[AT]",
 "K" : "[CA]",
 "M" : "[TG]",
 "B" : "[CGA]",
 "D" : "[ACT]",
 "H" : "[AGT]",
 "V" : "[TCG]",
 "N" : "[ATCG]"
}

def read_sequence(seq_file):
    f = file(seq_file,'r') #opens input file
    seq = '' 
    for l in f:
    	if l.startswith(">"):#skip header line
            continue 
        seq += l.rstrip().upper() 
    f.close() #closes input file
    return seq

def match(seq, dna_frag):
	fwd_pattern = ''
	for letter in range(len(dna_frag)):
		fwd_pattern += nt_code[dna_frag[letter]] #create regex for matching using dictionary
 	
 	regex_fwd = re.compile(fwd_pattern) 
 	count = 0
 	
 	for match in regex_fwd.finditer(seq):
 		count = count + 1 
 		position_num = '%s' % match.start()
 		print 'position is:', int(position_num)+1 #first position is 1 instead of 0 
 		print 'motif is:', '%s' % match.group() #the sequence of each forward match

 	rv_pattern = ''
 	for letter in range(len(dna_frag)):
 		rv_pattern += rev_nt_code[dna_frag[::-1][letter]]
 	
 	regex_rv = re.compile(rv_pattern)
 	
 	for match in regex_rv.finditer(seq):
 		count = count + 1
 		position_num = '%s' % match.start()
 		print 'position is:', int(position_num)+1
 		print 'motif is:', '%s' % match.group(), '(reverse strand)'#the sequence of each reverse match

 	print 'total number of matches is:', count #the number of matches

def main(seq_file, dna_frag):
    seq = read_sequence(seq_file)
    search = match(seq, dna_frag)

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2]) 

