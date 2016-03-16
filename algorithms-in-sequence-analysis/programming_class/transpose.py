#def myfunction(arg1,arg2, etc)
#def main()
    #input.sys.argv[ ]#etc
    #myfunction(arg1,arg2,etc...)

#if __name__ = "__main__":
    #main()
import sys

bases = ['T', 'C', 'A', 'G', 'U'] 
seq = input_file


	

def translate(input_file):
    f = open(input_file)
    codon_dict = {}
    for l in f:
	words = l.split()
	codon = words[0]
	letter = words[1]
	codon_dict[codon] = letter
    return codon_dict

 
def triplet(input_file):
    t = open(input_file)
    for i in range(0, len(t), 3):
	codon = seq[i:i+3]
	if len(codon) == 3:
	    print codon


    


	    
	
	
#start codon ATG, stop codons -- UAA, UGA, UAG	