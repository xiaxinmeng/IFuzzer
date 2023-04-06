class BadIterator() :
	def __iter__(self) :
		return self
	def __next__(self) : # should be __next__ for python 3.0
		del BadIterator.__next__
		return 1

itnext = BadIterator().__next__
print(itnext())
print(itnext())