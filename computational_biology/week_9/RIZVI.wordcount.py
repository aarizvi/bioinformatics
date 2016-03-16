import sys

rv_nuc = {
	"A" : "T",
	"T" : "A",
	"C" : "G",
	"G" : "C",
}

def read_sequence(seq_file):
    f = file(seq_file,'r') #opens input file
    seq = '' 
    for l in f:
    	if l.startswith(">"):#skip header line
            continue 
        seq += l.rstrip().upper().replace('U', 'T') 
    f.close() #closes input file
    return seq

def kmer(k, seq):
 	rev_seq = ''
 	for letter in range(len(seq)):
 		rev_seq += rv_nuc[seq[::-1][letter]]
	seq = seq + rev_seq
 
	f = {} #blank dictionary to put k-kmers in 
	total_kmers = len(seq) - k + 1
	for i in range(total_kmers):
		kmer = seq[i:i+k]
		f[kmer] = f.get(kmer, 0) + 1
	kmer = [key for key,val in f.iteritems() if val == max(f.values())] #collects max kmers
	maxkey = [val for key,val in f.iteritems() if val == max(f.values())] #collects max counts
	print 'max count:',max(maxkey)
	print 'max','%s%s' % (k,'-mers:'),'%s' % ' '.join(kmer)

def main(k,filename):
	seq = read_sequence(filename)
	kmers = kmer(int(k), seq)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])