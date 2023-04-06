class bad:
	def __init__(self):
		print("Creating", id(self))
	def __del__(self):
		print("Deleting", id(self))
	def __eq__(self, other):
		print("Comparing", id(self), "and", id(other))
		if be_bad:
			dict2.clear()
		return self is other
	def __hash__(self):
		return 0
be_bad = False
set1 = {bad()}
dict2 = {bad(): None}
be_bad = True
set1.symmetric_difference_update(dict2)