class Foo:
	def __init__(self):
		self.x = 1
	
	def __getattr__(self, name):
		if self.x:
			pass # etc...
	
	def __setattr__(self, name, val):
		if self.x:
			pass # etc...