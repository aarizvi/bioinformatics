#!/usr/bin/python
import thegame

#This initializes a new guessing game
#where the number is to be guessed between 1 and 100

game = thegame.TheGame(100)

#res == -1 if the number to guess is smaller
#res == 1 if the number to guess is bigger
#res == 0 if you won

#defining variables
UB = 100
LB = 0
number = ((UB + LB)/2)
res = 1
#loop
while res != 0:
    res = game.guess(number)
    if res == -1:
	UB = number
	number = ((UB + LB)/2)
    elif res == 1:
	LB = number
	number = ((UB + LB)/2)
	

	
	
	
	
	
	   
	
	
    
    

