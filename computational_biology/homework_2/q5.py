import sys

def read_sequence(seq_file):
    f = open(seq_file) #opens input file
    seq = f.read().rstrip().upper().replace('U','T') #reads input file, strips any unncessary spaces, makes sequence all uppercase, and replaces all Uracils with Thymines
    for l in seq: 
        if l not in 'AGCT': #error handling for invalid letters
            print 'Error: invalid sequence.'
            exit() #exits the program if there is an invalid sequence
    f.close #closes input file
    return seq 

def reverse_comp(seq):
    comp_dict = {'A':'T','T':'A','C':'G','G':'C'} #creates complementary strand dict
    comp_seq = '' #sets up new variable that will contain the comp. strand as a string after the for loop
    for letter in seq:
        comp_seq = comp_dict[letter] + comp_seq
    return comp_seq

def main(seq_file):
    seq = read_sequence(seq_file)
    print 'Forward:    5\'-',seq,'-3\''
    comp_seq = reverse_comp(seq)
    print 'Complement: 3\'-', comp_seq[::-1], '-5\''

if __name__ == "__main__":
    main(sys.argv[1])     #use sequence.txt as input file; so in command line: $ python q5.py sequence.txt