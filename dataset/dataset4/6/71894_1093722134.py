def generator():
	l = []
	yield l
	l.append(1)
	# this correctly prints 1
	print(len(l))