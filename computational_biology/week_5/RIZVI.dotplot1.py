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

def dotmatrix(sequences):
	seq1 = list(sequences[0]) #convert sequences to lists for convenient appending and accession of elements at specific indices
	seq2 = list(sequences[1])
	dotmat = [] #create an empty list that will gather the "information" (whether its a match (*) or not (empty space))
	dots = [] #empty list that will gather the full dotmatrix, but without newlines at each iteration

	for i in seq1[:-1]: #does not read the last element of the sequence list
		dotmat = [] #empties matrix for next iteration
		for j in seq2[:-1]:
			if i == j:
				star = '*'
				dotmat.append(''.join(star))
		 	else:
		 		space = ' '
		 		dotmat.append(''.join(space))
		dots.append(''.join(dotmat))  
	
	dotmatrix = [] #final matrix (list) that will be printed out with the newlines
	for line in dots:
		dotmatrix = '\n'.join(dots)  #puts newline at the end of each iteration 
	return dotmatrix

def main(input1, input2):
	sequences = readSequences(input1, input2)
	print "Seq. 1 is",sequences[0]
	print "Seq. 2 is",sequences[1]

	dot_matrix = dotmatrix(sequences)
	print dot_matrix

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])