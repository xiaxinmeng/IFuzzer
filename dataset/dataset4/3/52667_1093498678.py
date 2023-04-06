val = "a" * 10000
class big:
	def __repr__(self):
		return val
i = 16
while True:
	repr(frozenset(big() for j in range(i)))
	i = (i * 5) >> 2