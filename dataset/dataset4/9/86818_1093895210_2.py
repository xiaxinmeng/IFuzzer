import traceback

def foo():
	try:
		1/0
	except Exception as e:
		traceback.print_exc()
	finally:
		a = 1
		foo()	
		
foo()