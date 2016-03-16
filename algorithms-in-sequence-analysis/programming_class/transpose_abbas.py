import sys

def read_sequence(in_file):
    f = open(in_file) #opens input file
    seq = f.read().rstrip().upper() #reads input file
    f.close #closes input file
    return seq

#make a dictionary of 3 codon nucleotides into amino acids (codon_table.txt)        
def translate(input_file):
    f = open(input_file) #opens codon_table.txt
    codon_dict = {} #creates an empty dictionary that will translate the codons into amino acids
    for l in f:
        words = l.split()
        codon = words[0]
        letter = words[1]
        codon_dict[codon] = letter
    return codon_dict
 
def triplet(input_file):
    split = [] #creates empty list to add triplets with their amino acid
    x = ''
    seq = open(input_file) #grabs sequence file
    for i in range(seq[i:i+3]): #range from sequence from position 0 to 3 of the string
        if len(seq) == 3: #ensures that if the sequence has a 3 nucleotides in a split codon
            x = codon_dict[codon]
    split.append(x)        
    return split

def find_ORFs(seq, trans_dict):
    trans_list = [] #empty list that will have my translated list
    for j in range(0,3): #for loop to change starting position from 0 to 3 for ORF)
        ORF = seq[j:]
        x = ''
        translate = False
        for i in range(0, len(ORF), 3): 
            triplet = ORF[i:i+3] #defines variable triplet three successive nucleotides
            if len(triplet) == 3:  #if the codon is equal to 3 nucleotides, translate it
                amino_acid = trans_dict[triplet] #translates the codon sequence into amino acids
                if amino_acid == 'M': #if statement to define the start codon (Met)
                    translate = True
                elif amino_acid == '*': #if there is a stop codon (*) it will stop translation
                    translate = False
                if translate == True:
                    x += amino_acid #add the amino_acids to the empty string x
        trans_list.append(x) #add x to the empty list trans_list'
    return trans_list	    

def main(seq_file,dict_file):
    seq = read_sequence(seq_file)
    print seq #prints the sequence
    codon_dict = translate(dict_file)
    codon_list = triplet(split)
    print codon_list #prints the triplets of sequence and their amino acid codon pair

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2]) #argument 1 is the sequence file, argument 2 is the codon_table  
