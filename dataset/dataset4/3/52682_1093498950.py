class bad:
	def __eq__(self, other):
		global f2
		f2 = other
		print_f2()
		s1.add("querty")
		return self is other
	def __hash__(self):
		return hash(f1)
def print_f2():
	print(id(f2), repr(f2))
f1 = frozenset((1, 2, 3))
s1 = set(f1)
s1 in {bad()}
print_f2()