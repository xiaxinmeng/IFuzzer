import traceback
def foo():
	try:
		1/0
	except:
		traceback.print_exc()
	foo()
foo()