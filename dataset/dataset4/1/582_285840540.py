
class A(int):
	def __lt__(self, other):
		print("zebra")
		A.__lt__ = A.__false_lt__
		return int.__lt__(self, other)
	__true_lt__ = __lt__
	def __false_lt__(self, other):
		print("gizmo")
		A.__lt__ = A.__true_lt__
		return int.__lt__(self, other)
