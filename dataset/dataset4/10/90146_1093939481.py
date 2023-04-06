from typing import signature

def decorator(fun):
	print(signature(fun))
	return fun

class Test2:
	@decorator
	@staticmethod
	def test(arg):
		return arg