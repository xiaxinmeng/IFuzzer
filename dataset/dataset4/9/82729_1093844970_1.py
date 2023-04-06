from sympy.core import AtomicExpr
class MyWeirdClass(AtomicExpr):
	def __init__(self):
		pass
f = open("out.txt", "w")
f.write("abc\n")
exit(0)