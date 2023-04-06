def cell(o):
	def f(): o
	return f.__closure__[0]

def f():
	a = 1
	b = 2
	def g():
		return a + b
	return g

g = f()
