#!/usr/bin/python
# -*- coding: utf-8 -*-

#Students will need the import statements as example
import string
import BaumWelch
from BaumWelch import forward, backward, writeScoreMatrix, transitionP, emissionP, getProbabilityForwardX, baumWelch
import Viterbi
import AEMatrices
from AEMatrices import writeEMatrix,writeAMatrix
import Sequences

def main():
	#Read the A and E matrices
	AEMatrices.init("input/EmissionPriorE4.txt", "input/TransPriorA2.txt")
	#Read the input sequence(s) and store them into setX
	setX = Sequences.readSeq("input/sequences.txt", "X")
	maxIteration = 500
	sumLL = 0.0
	oldSumLL = 100000.0
	curIteration = 0
	#Stop if the change in log likelihood is less than a predefined threshold or that the maximum number of iterations is reached.

	while abs(sumLL - oldSumLL) > 0.01 and curIteration < maxIteration:
		oldSumLL = sumLL
		(newA, newE, sumLL) = BaumWelch.baumWelch(setX)
		AEMatrices.setNewA(newA) #will start from trained A 
		AEMatrices.setNewE(newE) 
		print 'Iteration: ',curIteration
		print 'Final transition matrix A',newA
		print 'Final emission matrix E',newE
		curIteration += 1
		print 'Current iteration sumLL: ',sumLL
	else:
		print 'The sequence has converged at iteration ',curIteration,' with a log likelihood of:' , sumLL
	

if __name__ == "__main__":
	main()
