#!/usr/bin/python

"""
Author: Anton Feenstra (feenstra@few.vu.nl)

Revision History:
File created on Nov 4, 2011

Template for dynamic programming excercises.

Copyright (c) 2011 Anton Feenstra
"""

# for commandline options:
from optparse import OptionParser, OptionGroup
from copy import deepcopy
import sys

# Built-in exchange matrices.
identity = [
    [ 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,],
]

pam250 = [
    [ 2, 0,-2, 0, 0,-4, 1,-1,-1, 0,-1,-2,-1, 0, 0, 1, 0,-2, 1, 1, 0, 0,-6, 0,-3, 0,],
    [ 0, 2,-4, 3, 2,-5, 0, 1,-2, 0, 1,-3,-2, 2, 0,-1, 1,-1, 0, 0, 0,-2,-5, 0,-3, 2,],
    [-2,-4,12,-5,-5,-4,-3,-3,-2, 0,-5,-6,-5,-4, 0,-3,-5,-4, 0,-2, 0,-2,-8, 0, 0,-5,],
    [ 0, 3,-5, 4, 3,-6, 1, 1,-2, 0, 0,-4,-3, 2, 0,-1, 2,-1, 0, 0, 0,-2,-7, 0,-4, 3,],
    [ 0, 2,-5, 3, 4,-5, 0, 1,-2, 0, 0,-3,-2, 1, 0,-1, 2,-1, 0, 0, 0,-2,-7, 0,-4, 3,],
    [-4,-5,-4,-6,-5, 9,-5,-2, 1, 0,-5, 2, 0,-4, 0,-5,-5,-4,-3,-3, 0,-1, 0, 0, 7,-5,],
    [ 1, 0,-3, 1, 0,-5, 5,-2,-3, 0,-2,-4,-3, 0, 0,-1,-1,-3, 1, 0, 0,-1,-7, 0,-5,-1,],
    [-1, 1,-3, 1, 1,-2,-2, 6,-2, 0, 0,-2,-2, 2, 0, 0, 3, 2,-1,-1, 0,-2,-3, 0, 0, 2,],
    [-1,-2,-2,-2,-2, 1,-3,-2, 5, 0,-2, 2, 2,-2, 0,-2,-2,-2,-1, 0, 0, 4,-5, 0,-1,-2,],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [-1, 1,-5, 0, 0,-5,-2, 0,-2, 0, 5,-3, 0, 1, 0,-1, 1, 3, 0, 0, 0,-2,-3, 0,-4, 0,],
    [-2,-3,-6,-4,-3, 2,-4,-2, 2, 0,-3, 6, 4,-3, 0,-3,-2,-3,-3,-2, 0, 2,-2, 0,-1,-3,],
    [-1,-2,-5,-3,-2, 0,-3,-2, 2, 0, 0, 4, 6,-2, 0,-2,-1, 0,-2,-1, 0, 2,-4, 0,-2,-2,],
    [ 0, 2,-4, 2, 1,-4, 0, 2,-2, 0, 1,-3,-2, 2, 0,-1, 1, 0, 1, 0, 0,-2,-4, 0,-2, 1,],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [ 1,-1,-3,-1,-1,-5,-1, 0,-2, 0,-1,-3,-2,-1, 0, 6, 0, 0, 1, 0, 0,-1,-6, 0,-5, 0,],
    [ 0, 1,-5, 2, 2,-5,-1, 3,-2, 0, 1,-2,-1, 1, 0, 0, 4, 1,-1,-1, 0,-2,-5, 0,-4, 3,],
    [-2,-1,-4,-1,-1,-4,-3, 2,-2, 0, 3,-3, 0, 0, 0, 0, 1, 6, 0,-1, 0,-2, 2, 0,-4, 0,],
    [ 1, 0, 0, 0, 0,-3, 1,-1,-1, 0, 0,-3,-2, 1, 0, 1,-1, 0, 2, 1, 0,-1,-2, 0,-3, 0,],
    [ 1, 0,-2, 0, 0,-3, 0,-1, 0, 0, 0,-2,-1, 0, 0, 0,-1,-1, 1, 3, 0, 0,-5, 0,-3,-1,],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [ 0,-2,-2,-2,-2,-1,-1,-2, 4, 0,-2, 2, 2,-2, 0,-1,-2,-2,-1, 0, 0, 4,-6, 0,-2,-2,],
    [-6,-5,-8,-7,-7, 0,-7,-3,-5, 0,-3,-2,-4,-4, 0,-6,-5, 2,-2,-5, 0,-6,17, 0, 0,-6,],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [-3,-3, 0,-4,-4, 7,-5, 0,-1, 0,-4,-1,-2,-2, 0,-5,-4,-4,-3,-3, 0,-2, 0, 0,10,-4,],
    [ 0, 2,-5, 3, 3,-5,-1, 2,-2, 0, 0,-3,-2, 1, 0, 0, 3, 0, 0,-1, 0,-2,-6, 0,-4, 3,],
]

blosum62 = [
    [ 4,-2, 0,-2,-1,-2, 0,-2,-1, 0,-1,-1,-1,-2, 0,-1,-1,-1, 1, 0, 0, 0,-3, 0,-2,-1,],
    [-2, 4,-3, 4, 1,-3,-1, 0,-3, 0, 0,-4,-3, 3, 0,-2, 0,-1, 0,-1, 0,-3,-4,-1,-3, 1,],
    [ 0,-3, 9,-3,-4,-2,-3,-3,-1, 0,-3,-1,-1,-3, 0,-3,-3,-3,-1,-1, 0,-1,-2,-2,-2,-3,],
    [-2, 4,-3, 6, 2,-3,-1,-1,-3, 0,-1,-4,-3, 1, 0,-1, 0,-2, 0,-1, 0,-3,-4,-1,-3, 1,],
    [-1, 1,-4, 2, 5,-3,-2, 0,-3, 0, 1,-3,-2, 0, 0,-1, 2, 0, 0,-1, 0,-2,-3,-1,-2, 4,],
    [-2,-3,-2,-3,-3, 6,-3,-1, 0, 0,-3, 0, 0,-3, 0,-4,-3,-3,-2,-2, 0,-1, 1,-1, 3,-3,],
    [ 0,-1,-3,-1,-2,-3, 6,-2,-4, 0,-2,-4,-3, 0, 0,-2,-2,-2, 0,-2, 0,-3,-2,-1,-3,-2,],
    [-2, 0,-3,-1, 0,-1,-2, 8,-3, 0,-1,-3,-2, 1, 0,-2, 0, 0,-1,-2, 0,-3,-2,-1, 2, 0,],
    [-1,-3,-1,-3,-3, 0,-4,-3, 4, 0,-3, 2, 1,-3, 0,-3,-3,-3,-2,-1, 0, 3,-3,-1,-1,-3,],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [-1, 0,-3,-1, 1,-3,-2,-1,-3, 0, 5,-2,-1, 0, 0,-1, 1, 2, 0,-1, 0,-2,-3,-1,-2, 1,],
    [-1,-4,-1,-4,-3, 0,-4,-3, 2, 0,-2, 4, 2,-3, 0,-3,-2,-2,-2,-1, 0, 1,-2,-1,-1,-3,],
    [-1,-3,-1,-3,-2, 0,-3,-2, 1, 0,-1, 2, 5,-2, 0,-2, 0,-1,-1,-1, 0, 1,-1,-1,-1,-1,],
    [-2, 3,-3, 1, 0,-3, 0, 1,-3, 0, 0,-3,-2, 6, 0,-2, 0, 0, 1, 0, 0,-3,-4,-1,-2, 0,],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [-1,-2,-3,-1,-1,-4,-2,-2,-3, 0,-1,-3,-2,-2, 0, 7,-1,-2,-1,-1, 0,-2,-4,-2,-3,-1,],
    [-1, 0,-3, 0, 2,-3,-2, 0,-3, 0, 1,-2, 0, 0, 0,-1, 5, 1, 0,-1, 0,-2,-2,-1,-1, 3,],
    [-1,-1,-3,-2, 0,-3,-2, 0,-3, 0, 2,-2,-1, 0, 0,-2, 1, 5,-1,-1, 0,-3,-3,-1,-2, 0,],
    [ 1, 0,-1, 0, 0,-2, 0,-1,-2, 0, 0,-2,-1, 1, 0,-1, 0,-1, 4, 1, 0,-2,-3, 0,-2, 0,],
    [ 0,-1,-1,-1,-1,-2,-2,-2,-1, 0,-1,-1,-1, 0, 0,-1,-1,-1, 1, 5, 0, 0,-2, 0,-2,-1,],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [ 0,-3,-1,-3,-2,-1,-3,-3, 3, 0,-2, 1, 1,-3, 0,-2,-2,-3,-2, 0, 0, 4,-3,-1,-1,-2,],
    [-3,-4,-2,-4,-3, 1,-2,-2,-3, 0,-3,-2,-1,-4, 0,-4,-2,-3,-3,-2, 0,-3,11,-2, 2,-3,],
    [ 0,-1,-2,-1,-1,-1,-1,-1,-1, 0,-1,-1,-1,-1, 0,-2,-1,-1, 0, 0, 0,-1,-2,-1,-1,-1,],
    [-2,-3,-2,-3,-2, 3,-3, 2,-1, 0,-2,-1,-1,-2, 0,-3,-1,-2,-2,-2, 0,-1, 2,-1, 7,-2,],
    [-1, 1,-3, 1, 4,-3,-2, 0,-3, 0, 1,-3,-1, 0, 0,-1, 3, 0, 0,-1, 0,-2,-3,-1,-2, 4,],
]

def parse_commandline():
    usage = "%prog <fasta> [options]"
    version = "0.0a"
    description = \
        "%prog aligns two sequences."
    epilog = \
        "Copyright (c) 2011 K. Anton Feenstra -- "\
        "feenstra@few.vu.nl -- www.few.vu.nl/~feenstra"
    parser = OptionParser(usage=usage, description=description,
                          version="%prog "+version, epilog=epilog)

    # sequence/alignment options:
    parser.add_option("-f", "--fasta",  dest="fasta", metavar="<file>",
                     help="input alignment file (fasta)")
    parser.set_defaults(fasta=None)
    
    parser.add_option("-e", "",  dest="exchange_matrix", 
                     help="Exchange matrix: pam250, blosum62 or identity (%default%)")
    parser.set_defaults(exchange_matrix="pam250")
    
    parser.add_option("-l", "",  dest="align_local",  action="store_true",
                     help="align local")
    parser.set_defaults(align_local=False)
    
    parser.add_option("-g", "",  dest="align_global", action="store_true",
                     help="align global")
    parser.set_defaults(align_global=False)
    
    parser.add_option("-s", "",  dest="align_semiglobal", action="store_true",
                     help="align semi-global")
    parser.set_defaults(align_semiglobal=False)
    
    parser.add_option("-p", "",  dest="gap_penalty", type="int",
                     help="Gap penalty (%default%)")
    parser.set_defaults(gap_penalty=2)
    
    parser.add_option("-v", dest="printmatrix", action="store_true",
                     help="print matrix score")
    parser.set_defaults(printmatrix = False)
    
    # get the options:
    (options, args) = parser.parse_args()

    if not options.fasta:
        # check if we have an option left (to be used as input filename):
        if args:
            options.fasta = args.pop()
        else:
            print "Need at least an input file (fasta)"
            print ""
            parser.print_help()
            print ""
            print "ERROR: no input file given"
            exit(-1)

    # check alignment type:
    align_options = [options.align_local, options.align_global, options.align_semiglobal]
    # check if at least one alignment option was true, else choose global
    if align_options.count(True)==0:
        print "No alignment type given, using Global"
        options.align_global=True
    # check if not more than one alignment option was true, else error and exit 
    if align_options.count(True)>1:
        print "ERROR: multiple alignment types chosen"
        exit(-1)

    # check for any leftover command line arguments:
    if len(args):
        warning("ignoring additional arguments "+str(args))
    
    # clean up (recommended):
    del(parser)
    return options

class Sequence:
    """Stores a sequence object"""
    
    def __init__(self, Label="", Sequence="" ):
        """Initialize a new Sequence object

        Label -- identifier of sequence (text)
        Sequence -- sequence string in single-letter alphabet
        """
        self.Label       = Label
        self.Sequence    = Sequence

    # this makes that you can do 'print sequence' and get nice output:
    def __str__(self):
        """Return string representation of a Sequence object"""
        # newline-delimited values of all the attributes
        return ">%s\n%s" % (self.Label, self.Sequence)


def readSequences(lines):
    """Return Sequences object
    
     -- list of lines or any object that behaves like it
    
    This routine parses a fasta file and returns a list of Sequence objects
    containing the sequences with label and sequence data set
    """
    seqs = []
    label = None
    seq_lines = []
    for line in lines:
        line = line.strip()      # strip off white space
        if not line:             # skip empty lines
            continue
        if line.startswith(';'): # ignore comment lines
            continue
        # check for start of next sequence:
        if line.startswith('>'): # label line
            # first, store the previous sequence if we had one:
            if seq_lines:
                seqs.append(Sequence(label, ''.join(seq_lines)))
                seq_lines = []
            # get the label (name) for the next sequence
            label = line[1:].strip()
        else:
            # collect all lines with sequence information for this sequence:
            seq_lines.append(line.upper()) #ensures that the sequence will read as uppercase from the fasta file
    # take care of the last sequence in the file
    seqs.append(Sequence(label, ''.join(seq_lines))) 
    return seqs

def do_global_alignment(sequences, matrix, penalty):
    """ do pairwise global alignment using DP """
    """matrix created by making list of lists"""
    score = [] 
    #ERROR HANDLING -- SAME FOR GLOBAL, SEMI, LOCAL
    try:
        for char in sequences[0].Sequence + sequences[1].Sequence: 
            if char == 'Z' or char == 'B':
                print "Error: Sequences have indistinguishable amino acids codes, e.g. Z (Glutamine or glutamic acid), B (Asparagine or Aspartic Acid"
                quit()    
            elif char == 'J' or char == 'O' or char == 'U' or char == 'X':
                print "Error: Sequences have invalid amino acid codes, e.g. 'J', 'O', 'U', 'X'"
                quit()
            elif type(char) == int:
                print "Error: An integer was found within the seqence, sequences can only contain proper amino acid letters."
                quit()
            else: 
                continue
    except IndexError:
        print 'Two sequences are required.  Check fasta file input.'
        quit() 

    for i in range(len(sequences[0].Sequence)+1): #initialization loop for rows
        score.append([i*(-penalty)]) #appends a list 0
    for j in range(1,len(sequences[1].Sequence)+1): #initialization loop for columns 
        score[0].append(j*(-penalty)) #appends a list of 0s to element 0 of score
    
    for row in range(1,len(sequences[0].Sequence)+1): #extending template for entries matrix 
        for col in range(1,len(sequences[1].Sequence)+1): #filling out rest of scoring matrix from all directions
            xcmatrix = matrix[ord(sequences[0].Sequence[row-1]) - ord("A")][ord(sequences[1].Sequence[col-1]) - ord("A")]  #ord adds a unicode to a character
            match = score[row-1][col-1] + xcmatrix 
            mismatch_up = score[row][col-1] - penalty
            mismatch_left = score[row-1][col] - penalty
            
            score[row].append(max(match,mismatch_up,mismatch_left)) #adds maximum score (between diag, right and down) to matrix
    return score

def do_semiglobal_alignment(sequences, matrix, penalty):
    """matrix was created similarly to global_alignment"""
    """semi-global alignment initalization loops do not contain penalties"""
    score = []
    try:
        for char in sequences[0].Sequence + sequences[1].Sequence: 
            if char == 'Z' or char == 'B':
                print "Error: Sequences have indistinguishable amino acids codes, e.g. Z (Glutamine or glutamic acid), B (Asparagine or Aspartic Acid"
                quit()    
            elif char == 'J' or char == 'O' or char == 'U' or char == 'X':
                print "Error: Sequences have invalid amino acid codes, e.g. 'J', 'O', 'U', 'X'"
                quit()
            elif type(char) == int:
                print "Error: An integer was found within the seqence, sequences can only contain proper amino acid letters."
                quit()
            else: 
                continue
    except IndexError:
        print 'Two sequences are required.  Check fasta file input.'
        quit() 

    for i in range(len(sequences[0].Sequence)+1): 
        score.append([0]) #there is no initalization loop for semi-global so 0s are appended
    for j in range(1,len(sequences[1].Sequence)+1): 
        score[0].append(0) #appending 0s into the 0th (first) element of the list --> making a list of lists

    for row in range(1,len(sequences[0].Sequence)+1): 
        for col in range(1,len(sequences[1].Sequence)+1): 
            xcmatrix = matrix[ord(sequences[0].Sequence[row-1]) - ord("A")][ord(sequences[1].Sequence[col-1]) - ord("A")] 
            match = score[row-1][col-1] + xcmatrix
            mismatch_up = score[row][col-1] - penalty
            mismatch_left = score[row-1][col] - penalty
            score[row].append(max(match,mismatch_up,mismatch_left)) #adds maximum score (between diag, right and down) to matrix
    return score #this matrix will be used 

def do_local_alignment(sequences, matrix, penalty):
    """matrix was created similarly to global_alignment"""
    score = []
    try:
        for char in sequences[0].Sequence + sequences[1].Sequence: 
            if char == 'Z' or char == 'B':
                print "Error: Sequences have indistinguishable amino acids codes, e.g. Z (Glutamine or glutamic acid), B (Asparagine or Aspartic Acid"
                quit()    
            elif char == 'J' or char == 'O' or char == 'U' or char == 'X':
                print "Error: Sequences have invalid amino acid codes, e.g. 'J', 'O', 'U', 'X'"
                quit()
            elif type(char) == int:
                print "Error: An integer was found within the seqence, sequences can only contain proper amino acid letters."
                quit()
            else: 
                continue
    except IndexError:
        print 'Two sequences are required.  Check fasta file input.'
        quit() 

    for i in range(len(sequences[0].Sequence)+1): 
        score.append([0]) 
    for j in range(1,len(sequences[1].Sequence)+1): 
        score[0].append(0)
    
    #local alignment will not report negative numbers, if there are negative numbers it will be returned as zero
    for row in range(1,len(sequences[0].Sequence)+1): 
        for col in range(1,len(sequences[1].Sequence)+1): 
            xcmatrix = matrix[ord(sequences[0].Sequence[row-1]) - ord("A")][ord(sequences[1].Sequence[col-1]) - ord("A")] 
            match = score[row-1][col-1] + xcmatrix
            if match < 0: #ensures that all negatives are reported as 0
                match = 0   
            mismatch_up = score[row][col-1] - penalty
            if mismatch_up < 0: #ensures that all negatives are reported as 0
                mismatch_up = 0
            mismatch_left = score[row-1][col] - penalty
            if mismatch_left < 0: #ensures all negatives are reported as 0
                mismatch_left = 0
            score[row].append(max(match,mismatch_up,mismatch_left)) #adds maximum score (between diag, right and down) to matrix
    return score    

def print_matrix(raw_mat, sequences):
    mat = deepcopy(raw_mat) #the sequence list is mutable, so we need to have a copy of the matrix that wasn't changed from the alignments
    seq_2 = ('-' + sequences[1].Sequence)  #'-' indicates that we start scoring with a gap
    mat.insert(0, list(seq_2)) #inserting the shorter sequence (Sequence 2) to the matrix, it needs to be a list so all elements of the sequence can be added separately 

    seq_1 = list(' ' + '-' + sequences[0].Sequence) #the initial string space is added so our matrix is aligned properly

    for i in range(len(mat)): #iterate through the length of the matrix
        length_seq1 = seq_1[i] #selects the correct amino acid to align with the correct column for alignment scoring
        matrix_index = mat[i] #creates an index of the length of the matrix
        insert_seq1 = matrix_index.insert(0,length_seq1) #properly aligns the amino acid sequence to the scoring matrix
   
    for row in mat:
        pretty_matrix = '' 
        for col in row:
            pretty_matrix += '%5s' % (str(col)) #makes the width of printed characters spaced 5 apart
        print pretty_matrix

def traceback(mat, sequences, penalty, exchangeMatrix):
    options = parse_commandline()
    alignseq1 = '' 
    alignseq2 = ''

    seq1 = sequences[0].Sequence
    seq2 = sequences[1].Sequence

    i = len(seq1)
    j = len(seq2)
    #for c in range(i): #iterate through the length of the matrix
    #construct aligned sequences from right to left
    #test whether current entry equals diag plus exchange value 
    if options.align_global:
        ali_score = mat[i][j]
        while i > 0 or j > 0:   #repeat process until you are in upper left corner of matrix 
                score = mat[i][j] #check where in matrix you came from (left,above,diag), start from bottom-right matrix entry
                scorediag = mat[i-1][j-1]
                scoreup = mat[i-1][j]
                scoreleft = mat[i][j-1]

                if score == scorediag + exchangeMatrix[ord(seq1[i-1]) - ord("A")][ord(seq2[j-1]) - ord("A")]:
                    alignseq1 = seq1[i-1] + alignseq1     #prepend matched residues
                    alignseq2 = seq2[j-1] + alignseq2    #prepend matched residues
                    i -= 1 
                    j -= 1
                elif score == scoreup - penalty:
                    alignseq1 = seq1[i-1] + alignseq1     #prepend matched residues
                    alignseq2 = '-' + alignseq2     #prepend gap as '-' to one sequence and the corresponding to the other
                    i -= 1
                elif score == scoreleft - penalty:
                    alignseq1 = '-' + alignseq1     #prepend gap as '-' to one sequence and the corresponding to the other
                    alignseq2 = seq2[j-1] + alignseq2       #prepend matched residues
                    j -=1
                else: 
                    print 'Error'
       
    elif options.align_semiglobal:    
        #semi-global alignment takes the best score from the last row or last column.  
        last_row = mat[i]
        last_col = []
        for col in mat:
            last_col.append(col[j])  #append the last
        maxcol = max(last_col) #highest score of last column
        maxrow = max(last_row) #highest score of last row
        ali_score = max(maxcol, maxrow) #highest score of either last row, or last column

        if ali_score in last_row and ali_score in last_col:
            i_dist = 0 
            j_dist = 0
            for x in range(i)[::-1]: #inverses the order that the length is being read so that it can be read from the bottom corner up
                i_dist += 1 #moves up one row (in a column) 
                if last_col[x] == maxcol:  #if the position in the column equals the greatest score then i=x
                    i = x 
                    break
            for y in range(j)[::-1]: #starts in the bottom row
                j_dist += 1 #moves to the left one column
                if last_row[y] == maxrow: #if the position in the row equals the max row score, then j = y
                    j = y
                    break
            if j_dist < i_dist: #if the distance of from the corner to the max score in the row than the column then: 
                i = len(seq1) #i will be the length of seq 1
            else:
                j = len(seq2)
        elif ali_score in last_col: #otherwise just find the max score in the column and starta traceback from there
            for x in range(i)[::-1]:
                if last_col[x] == maxcol:
                    i = x
                    break
        elif ali_score in last_row: #otherwise just find the highest score in the last row and start traceback from there
            for y in range(j)[::-1]:
                if last_row[y] == maxrow:
                    j = y
                    break
        """i and j have been changed so the lengths of the seq1 and seq2 needed to be reassigned"""            
        lseq1 = len(seq1) 
        lseq2 = len(seq2)

        while i > lseq1 or j > lseq2: #adjusts for different sequence lengths 
            if i < lseq1:  
                alignseq1 = sequences[0].Sequence[lseq1-1] + alignseq1
                alignseq2 = '-' + alignseq2 
                lseq1 -= 1
            elif j < lseq2:
                alignseq2 = sequences[1].Sequence[lseq2-1] + alignseq2
                alignseq1 = '-' + alignseq1
                lseq2 -= 1

        while i > 0 and j > 0: 
            score = mat[i][j] #check where in matrix you came from (left,above,diag), start from bottom-right matrix entry
            scorediag = mat[i-1][j-1]
            scoreup = mat[i-1][j]
            scoreleft = mat[i][j-1]

            if score == scorediag + exchangeMatrix[ord(seq1[i-1]) - ord("A")][ord(seq2[j-1]) - ord("A")]:
                alignseq1 = seq1[i-1] + alignseq1     #prepend matched residues
                alignseq2 = seq2[j-1] + alignseq2     #prepend matched residues
                i -= 1
                j -= 1
            elif score == scoreup - penalty:
                alignseq1 = seq1[i-1] + alignseq1     #prepend matched residues
                alignseq2 = '-' + alignseq2     #prepend gap as '-' to one sequence and the corresponding to the other
                i -= 1
            elif score == scoreleft - penalty:
                alignseq1 = '-' + alignseq1     #prepend gap as '-' to one sequence and the corresponding to the other
                alignseq2 = seq2[j-1] + alignseq2       #prepend matched residues
                j -=1

        while i > 0 or j > 0: #while loop makes sures that gaps are properly added to the alignment 
            score = mat[i][j]
            if j == 0 and score == mat[i-1][j] - penalty or mat[i-1][j] == 0:
                alignseq1 = sequences[0].Sequence[i-1] + alignseq1
                alignseq2 = '-' + alignseq2
                i -= 1
            elif i == 0 and score == mat[i][j-1] - penalty or mat[i][j-1] == 0:
                alignseq1 = '-' + alignseq1
                alignseq2 = sequences[1].Sequence[j-1] + alignseq2
                j -= 1

    elif options.align_local:
        ali_score = max(max(row) for row in mat) #max number in the last row of the matrix is the alignment score 
        for row, column in ((x,y) for x in range(i) for y in range(j)):
            if mat[row][column] == ali_score:  
                i = row
                j = column 
            else:
                continue

        while mat[i][j] > 0:
            score = mat[i][j] #check where in matrix you came from (left,above,diag), start from bottom-right matrix entry
            scorediag = mat[i-1][j-1]
            scoreup = mat[i-1][j]
            scoreleft = mat[i][j-1]
            if score == scorediag + exchangeMatrix[ord(seq1[i-1]) - ord("A")][ord(seq2[j-1]) - ord("A")]:
                alignseq1 = seq1[i-1] + alignseq1     #prepend matched residues
                alignseq2 = seq2[j-1] + alignseq2    #prepend matched residues
                i -= 1
                j -= 1
            elif score == scoreup - penalty:
                alignseq1 = seq1[i-1] + alignseq1     #prepend matched residues
                alignseq2 = '-' + alignseq2     #prepend gap as '-' to one sequence and the corresponding to the other
                i -= 1                
            elif score == scoreleft - penalty:
                alignseq1 = '-' + alignseq1     #prepend gap as '-' to one sequence and the corresponding to the other
                alignseq2 = seq2[j-1] + alignseq2       #prepend matched residues
                j -=1
            else: 
                 print 'Error'

    vert_bar = '' #creating an empty string to add | to represent an alignment 

    for letter in range(len(alignseq1)): 
        if alignseq1[letter] == alignseq2[letter] == '-':  #if the letters are gaps leave an empty space
            vert_bar += ' '
        elif alignseq1[letter] != alignseq2[letter]: #if the letters don't match, put a space
            vert_bar += ' '
        elif alignseq1[letter] == alignseq2[letter]: #if the letters are matched put a vertical bar |
            vert_bar += '|'


    print 'Alignment 1: ', ' '.join(list(alignseq1))     #print aligned sequence 1
    print '             ',' '.join(list(vert_bar))      # print a line w/ vertical bars between residues
    print 'Alignment 2: ', ' '.join(list(alignseq2))    #print aligned sequence 2
    print 'Score =', ali_score    #print score    

# main function:
def main():
    # get command line options
    options = parse_commandline()

    # set substitution matrix:
    if options.exchange_matrix == "pam250":
        exchangeMatrix = pam250
    elif options.exchange_matrix == "blosum62":
        exchangeMatrix = blosum62
    elif options.exchange_matrix == "identity":
        exchangeMatrix = identity
    else:
        print "unknown exchange matrix", options.exchange_matrix
        exit(-1)
    
    # read sequences from fasta file, and catch error reading file
    try:
        sequences = readSequences(open(options.fasta))
    except IOError:
        print "ERROR: cannot open or read fasta input file:", fastafile
        exit(-1)


    for seq in sequences:
        print seq
    
    # call alignment routine(s):
    if options.align_global:
        score=do_global_alignment(sequences, exchangeMatrix, options.gap_penalty)         
    elif options.align_local:
        score=do_local_alignment(sequences, exchangeMatrix, options.gap_penalty)
    elif options.align_semiglobal:
        score=do_semiglobal_alignment(sequences, exchangeMatrix, options.gap_penalty)
    else:
        print "BUG! this should not happen."
        exit(-1)
    
    
    # do something with the score matrix from the alignment
    if options.printmatrix:
        print_matrix(score,sequences)
    else:
        print "Add -v option for scoring matrix"   
        
    #traceback 
    traceback(score,sequences,options.gap_penalty,exchangeMatrix) 

if __name__ == "__main__":
    main()
# last line
