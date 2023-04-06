class C():
	__slots__ = ('a',)
	def __new__(cls, a):
		self = object.__new__(cls)
		self.a = a
		return self
c = C(1)