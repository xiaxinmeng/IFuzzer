import copy

class Foo:
	def __init__(self, fn=None):
		self.fn = fn

class Bar:
	d = {'foobar': Foo(fn=lambda x: x*x)}
	
	def cp(self):
		self.xerox = copy.deepcopy(self.d)