############## SAMPLE USE CASE ##############
import pdb

def square(i):
	pdb.set_trace(trigger=not isinstance(i, (float, int)))
	print(i**2)

# debug: hunting for TypeError
a = 2
square(a) # will not execute set_trace()
b = None
square(b) # will execute set_trace()