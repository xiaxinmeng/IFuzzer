class MyBytes(bytes):
	pass
class C(object):
	def __bytes__(self):
	    return MyBytes(b"hello world")
MyBytes(C()) # fails the assert
