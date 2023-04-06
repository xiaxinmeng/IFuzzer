class B(object):
	def __int__(self):
	    return 43.0

class A(object):
	def __trunc__(self):
	    return B()

int(A())
