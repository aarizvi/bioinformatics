import sys

def comp(expr):
    op = expr[0]
    if op == "abs":
	a = float(expr[1])
	return abs(a)
    else:
	a = float(expr[1])
	b = float(expr[2])
	if op == "add":
	    return add(a,b)
	elif op == "sub":
	    return sub(a,b)
	elif op == "fdiv":
	    return fdiv(a,b)
	elif op == "mult":
	    return mult(a,b)
	else:
	    return "Invalid operator!"

