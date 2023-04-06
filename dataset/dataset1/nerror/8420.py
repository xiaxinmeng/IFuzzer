class bad:
	def __eq__(self, other):
		if be_bad:
			set2.clear()
			raise Exception
		return self is other
	def __hash__(self):
		return 0
be_bad = False
set1 = {bad()}
set2 = {bad() for i in range(2000)}
be_bad = True
set1.update(set2)
