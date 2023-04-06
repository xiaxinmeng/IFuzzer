import sys

def f():
    for i in range(5):
        print (i)      # line tracing will raise an exception at line 5

def g(frame, why, extra):
    if why == 'line' and frame.f_lineno == 5:
        raise "i am crashing"
    return g



sys.settrace(g)
f()

 	  	 
