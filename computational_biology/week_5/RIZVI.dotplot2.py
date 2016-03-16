import sys

def readSequences(file1,file2):
	sequence1 = open(file1)
	sequence2 = open(file2)
	seq1 = "" #create an empty string to append sequence to 
	for line in sequence1:
		if not line.startswith('>'): #skip the first line of fasta file
			seq1 += line.strip().upper() #append the sequence to empty string, strips any underwanted spaces, makes all uppercase incase of lowercase seq elements	
	seq2 = ""
	for line in sequence2:
		if not line.startswith('>'):
			seq2 += line.strip().upper()
	return seq1, seq2


def slider(sequences, window):
	window = int(window) #reads window as integer

	seq1_list = list(sequences[0])
	seq1 = seq1_list[:-1] #don't want last character
	seq1result = []
	for i in range(len(seq1)):
		#calculate start and stop
		start = 0 + i 
		stop = i + window
		seq1result.append(seq1[start:stop])

	seq2_list = list(sequences[1])
	seq2 = seq2_list[:-1]
	seq2result = []
	for j in range(len(seq2)):
		start = 0 + j 
		stop = j + window
		seq2result.append(seq2[start:stop])	
	return seq1result, seq2result


def dotmatrix(seq1, seq2, window, cutoff):
	dotmat = [] #create an empty list that will gather the "information" (whether its a match (*) or not (empty space))
	dots = [] #empty list that will gather the full dotmatrix, but without newlines at each iteration

	for i in seq1: #does not read the last element of the sequence list
		for j in seq2:
			if i == j:
				star = '*'
				dotmat.append(''.join(star))
		 	else:
		 		space = ' '
		 		dotmat.append(''.join(space))
		dots.append(''.join(dotmat)) 
		dotmat = [] #empties matrix for next iteration 
	
	dotmatrix = [] #final matrix (list) that will be printed out with the newlines
	for line in dots:
		dotmatrix = '\n'.join(dots)  #puts newline at the end of each iteration 
	return dotmatrix


def main(input1, input2, window, cutoff):
	sequences = readSequences(input1, input2)
	print "Seq. 1 is",sequences[0]
	print "Seq. 2 is",sequences[1]
	seqwin = slider(sequences, window)
	seq1win = seqwin[0]
	print 'Window:', window, "Cutoff:", cutoff
	seq2win = seqwin[1]

	dot_matrix = dotmatrix(seq1win, seq2win, window, cutoff)
	print dot_matrix

if __name__ == "__main__":
    if 0 <= sys.argv[3] > sys.argv[4]:
    	main(sys.argv[1],sys.argv[2], sys.argv[3], sys.argv[4])
    else:
    	raise Exception, 'Window is greater than cutoff'





