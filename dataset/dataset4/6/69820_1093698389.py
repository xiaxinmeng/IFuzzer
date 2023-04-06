class Descriptor(): 
	def __get__(self, instance, owner=None): 
		raise AttributeError('Implicitly suppressed')

class A(): 
	d = Descriptor()
	def __getattr__(self, name): 
		return 'default'