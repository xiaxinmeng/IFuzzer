import sys

def f():
	try:
	    raise ValueError    # line 5
	except ValueError:
	    print(42)           # line 7

def my_trace(*args):
	print(args)
	if args[1] == 'line':
	    f = args[0]
	    if f.f_lineno == 5:
	        f.f_lineno = 7
	return my_trace

sys.settrace(my_trace)
f()
sys.settrace(None)
