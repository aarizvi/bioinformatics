#!usr/bin/python
import sys

def add(a,b):
    return a+b
    
def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def fdiv(a,b):
    return a/b
    
def fact(n):
    answer = 1
    for i in range(1,int(n)+1):
	answer=answer*i
    return answer

def sum(k,n):
    answer = 0
    for i in range(int(k),int(n)+1):
	answer=answer+i
    return answer
    
def error_msg(i):
    if   i == 1: return "Error: Invalid operations - use: add, sub, fdiv, mult, sum"
    elif i == 2: return "Error: Need more input arguments"
    else:        return "Unexpected error occurred"

def comp(expr):
    try:
	op = expr[0]
	a = float(expr[1])
	if op == "abs":
	    return abs(a)
	elif op == "fact":
	    return fact(a)
	else:
	    b = float(expr[2])
	    if op == "add":
		return add(a,b)
	    elif op == "sub":
		return sub(a,b)
	    elif op == "fdiv":
		return fdiv(a,b)
	    elif op == "mult":
		return mult(a,b)
	    elif op == "sum":
		return sum(a,b)
	    else:
		return error_msg(1)
    except IndexError:
	return error_msg(2)
    except:
	return error_msg(3)

print sys.argv
if __name__ == "__main__":
    print comp(sys.argv[1:])

