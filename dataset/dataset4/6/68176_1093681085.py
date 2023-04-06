class C(object):
	def __init__(self, a, b=2, c=3):
		pass

class D(C):
	def __init__(self, d, **kwargs):
		super(D, self).__init__(**kwargs)

class E(D):
	def __init__(self, **kwargs):
		super(E, self).__init__(**kwargs)

E(d=42, b=0, c=0)