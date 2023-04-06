def foo():
	try:
		1/0
	except:
		pass
	foo()
foo()