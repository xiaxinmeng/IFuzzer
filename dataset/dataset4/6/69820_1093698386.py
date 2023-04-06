class A(): 
	def __init__(self, x=None): 
		self.x = x

	@property
	def t(self): 
		return self.x.t

	def __getattr__(self, name): 
		return 'default'