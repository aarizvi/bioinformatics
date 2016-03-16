#s!/usr/bin/python
# -*- coding: utf-8 -*-

import string
import math
import AEMatrices
from AEMatrices import A, E, allStates, emittingStates, emissionSymbols, writeEMatrix, writeAMatrix

# Forward algorithm, takes a sequence X and the nr. of symbols in of the sequence (L) as inputs
# It uses  A, E, allStates, emittingStates, emissionSymbols from AEMatrices
# Output: forward matrix (in form of dictionary)
# usage example: f = forward(sequence, L)
# f[k][i], forward of state k, at sequence position i
# note that we count from 0,1,2...,L,L+1
# where 0 indicates the begin state and L+1 the end state
def forward(X):
	L = len(X)-2
	f = dict()
	# initialize f to '0'  - sets all States for all positions to 0
	for k in allStates:
		f[k] = [0]*(L+2)
	# initialize begin state
	f['B'][0]=1  
	###start coding here###
	# iterate over sequence
	
	for i in range(1,L+1): # from first letter in seq to last letter in seq
		for l in emittingStates:
			result = 0
			# find sum  of vi[k][i-1]*A[k][l]
			for k in allStates:
				result += f[k][i-1]*A[k][l]
			f[l][i]=result * E[l][X[i]]

	#calculate f for End state at position L-1
	prob_fwd = 0
	for l in emittingStates:
		prob_fwd = prob_fwd + f[l][L] * A[l]['E']
	f['E'][L+1]=prob_fwd
	#return forward matrix
	###end coding here###
	return f
	
#write to matrix
#writePathMatrix(b,X,"output/BackwardMatrix.txt")
#print probability backwards = = +str(total_sum_end)
def writeScoreMatrix(M, X, filename):
	f = open(filename, "w")
	print>>f, "\t",
	for n in range(0, len(X)):
		print>>f, n, "\t",
	print>>f, "\n\t",
	for i in X:
		if i == " ":
			print>>f, "-\t",
		else :
			print>>f, i, "\t",
	print>>f  
	for state in allStates:
		print>>f, state,"\t",
		for i in range(0,len(X)):
			print>>f, M[state][i], "\t",
		print>>f
	print "written ", filename
	
# Backward algorithm, takes a sequence X and the nr. of symbols in of the sequence (L) as inputs
# It uses  A, E, allStates, emittingStates, emissionSymbols from AEMatrices
# Output: backward matrix (in form of dictionary)
# usage example: b = backward(sequence, L)
# b[k][i], backward of state k, at sequence position i
# note that we count from L+1,L,....,2,1,0  
# where 0 indicates the begin state and L+1 the end state
def backward(X):
	L = len(X)-2
	#switch k and l
	#probability of foward should match backwards
	b=dict()
	# initialise b to '0' 
	for k in allStates:
		b[k] = [0]*(L+2)
	# initialise end state
	for k in allStates:
		b[k][L]=A[k]['E']  
	###start coding here###
	# iterate over sequence
	for i in range(L-1,0,-1):
		for l in allStates:
			#find sum  of vi[k][i-1]*A[k][l]
			#sum scores from all index+1 states for current index state
			#multiply by emission probabilities of index + 1
			for k in emittingStates:
				b[l][i] += b[k][i+1]*A[l][k]*E[k][X[i+1]]
	
	#calculate probability for B state at 0 index
	prob_back = 0
	for l in emittingStates:
		result = b[l][1] * A['B'][l] * E[l][X[1]]
		prob_back += result
	b['B'][0]=prob_back #probability of X1|HMM
	#write to matrix
	#writePathMatrix(b,X,"output/BackwardMatrix.txt")
	#print probability backwards = = +str(prob_back)
	### end coding here###
	return b

# Calculate the transition probability from state k to state l given the training sequence X and forward and backward matrix of this sequence.
# Output: Transition probability matrix (in form of dictionary)
def transitionP(f,b,X):
	L = len(X)-2
	aP=dict()
	# initialise aP 
	for k in allStates:
		aP[k] = dict()
		for l in allStates:
			aP[k][l]=0;
	# iterate over sequence
	for i in range(0,L):
		for k in allStates:
			for l in emittingStates:
				###start coding here###
				# calculate probability of transition k->l at position i
				aP[k][l] += f[k][i] * A[k][l] * E[l][X[i+1]] * b[l][i+1]
				###end coding here###
	# add transition to end state                                     
	for k in allStates:
		aP[k]['E']= aP[k]['E'] + f[k][L]*A[k]['E']
	return aP

#Calculate the emission probability of symbol s from state k given the training sequence X and forward and backward matrix of this sequence.
#Output: Emission probability matrix (in form of dictionary)
def emissionP(f,b,X):
	L = len(X)-2
	eP=dict()
	# initialise tP 
	for k in allStates:
		eP[k] = dict()
		for s in emissionSymbols:
			eP[k][s]=0;
	# iterate over sequence
	for i in range(1,L+1):
		for k in allStates:
			###start coding here###
			# calculate probability symbol s at state k
			eP[k][X[i]] += f[k][i] * b[k][i]
			###end coding here###
	return eP

#returns probability given the forward matrix
def getProbabilityForwardX(f,L):
	return (f['E'][L+1])
    
# Baum-Welch algorithm, takes a set of training sequences setX as input
# Output: the new A matrix, new E matrix and the total sum of the log likelihood, all in a single list
# usage example: (newA, newE, sumLL) = baumWelch(setX)
def baumWelch(setX):
	# initialize emission counts matrix
	# eC[k][s] is the expected number of counts for emission symbol s
	# at state k
	eC = dict()
	for k in allStates:
		eC[k] = dict()
		for s in emissionSymbols:
			#you may want to add pseudo counts here
			eC[k][s]=0;

	# initialize transition count matrix
	# aC[k][l] is the expected number of transitions from
	# state k to state l
	aC = dict()
	for k in allStates:
		aC[k] = dict()
		for l in allStates:
			#you may want to add pseudo counts here
			aC[k][l]=0;

	sumLL=0.0
	# iterate over training sequences
	for X in setX:      
		L = len(X)-2
		##start coding here###
		## you may use the following functions defined above: 
		## forward, backward, getProbabilityFowardX, emissionP, transitionP
		## here you should calculate eC and aC,
		## the matrices for the number of expected counts
		## also calculate your sumLL, the sum over the logodds
		### of all the sequences in the training set. Wera
		f = forward(X)
		b = backward(X)
		probability = getProbabilityForwardX(f,L)
		sumLL += math.log(probability,2)
		aP = transitionP(f,b,X)
		eP = emissionP(f,b,X)		

	
	# add transition counts
		for l in allStates:
			for k in allStates:
				aC[k][l] += aP[k][l]/probability
	
	#add emission counts
		for k in allStates:
			for s in emissionSymbols:
				eC[k][s] += eP[k][s]/probability		
	###end coding here###
	#finish iteration
    

	#calculate new transitions --> maximum likelihood estimators 
	#initialize new transition matrix newA
	###just generate the training sequences and count the number of transitions from state k to l and make it a probability 
	###through dividing by the total number of transitions out of state k
	newA = dict()
	for k in allStates:
		newA[k]=dict()
		sum_l=0
		##start coding here###
		## here you should calculate your new transition 
		## matrix newA
	for l in allStates:
		sum_l = 0 
		for k in allStates:  
			sum_l += aC[l][k]
		for k in allStates:
			try:
				newA[l][k] = aC[l][k]/sum_l 
			except ZeroDivisionError:
				newA[l][k] = 0 
		##end coding here###
        
	# calculate new emissions
	###just generate the training sequences and count the number of emissions of a given symbol 
	###in state k and make it a probability by normalising using the total number of emissions of 
	###state k (the number of state visits)
	# initialize new emission matrix newE
	newE = dict()
	for k in emittingStates:
		newE[k] = dict()
		sum_s=0
		for s in emissionSymbols:
			sum_s += eC[k][s]
		for s in emissionSymbols:
			try:
				newE[k][s] = eC[k][s]/sum_s
			except ZeroDivisionError:
		 		newE[k][s] = 0
		###start coding here###
		###here you should calculate your new emission 
		###matrix newE
		###end coding here###   
	return (newA, newE, sumLL)
# finish BaumWelch
