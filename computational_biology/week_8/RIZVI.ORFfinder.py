import sys
from codondictionary import codon_dictionary #codondictionary.py has to be your in working directory for this module to work correctly


def read_sequence(seq_file):
    f = file(seq_file,'r') #opens input file
    seq = '' #reads input file, strips any unncessary spaces, makes sequence all uppercase, and replaces all Uracils with Thymines
    for l in f:
    	if l.startswith(">"):   # skip header line
            continue 
        seq += l.rstrip().upper().replace('U','T')
    f.close() #closes input file
    return seq

#get complementary strands of the original sequences
def find_complement(seq):
    comp_dict = {'A':'T','T':'A','C':'G','G':'C'} #creates complementary strand dict
    comp_seq = [] #sets up new variable that will contain the comp. strand as a string after the for loop
    for letter in range(len(seq)):
        comp_seq.append(comp_dict[seq[letter]])
    return ''.join(comp_seq[::-1])

def find_ORFs(seq, comp_seq):
    frames = ['','','','','','']
    #3 forward frames
    for i in range(0, len(seq) - 3): #last codon begins 3 bases from the end
        framenum = i % 3 #designates the current frame 
        frames[framenum] += codon_dictionary[seq[i:i+3]]

    # 3 reverse frames
    for i in range(0, len(comp_seq) - 3):
        framenum = 5 - i % 3 #designate reverse reading frame
        frames[framenum] += codon_dictionary[comp_seq[i:i+3]]        
    count = 0
    for framenum in range(len(frames)): #split ORFs for each frame using "_" delimiter (stop codon = '-'), save > 15aa 
        ORFs = [x for x in frames[framenum].split('_') if len(x) > 15]
        for pepseq in ORFs:
            count += 1
            print 'ORF',framenum+1,':',pepseq,'length:',len(pepseq)
            #framenum + 1 because the list starts are 0 ... so 0 is the 1st frame

def main(seq1, seq2):
    seq1 = read_sequence(seq1)
    comp_seq1 = find_complement(seq1)
    print "SEQUENCE A:", seq1
    frames1 = find_ORFs(seq1, comp_seq1)

    seq2 = read_sequence(seq2)
    comp_seq2 = find_complement(seq2)
    print "SEQUENCE B:", seq2
    frames2 = find_ORFs(seq2, comp_seq2)

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2]) 
