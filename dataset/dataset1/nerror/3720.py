# this example crashes in python 2.5.2 (amd64 ubuntu heron, 29 august 2008)
# python 3.0b3, with __next__ rather than next, also crashes

class A(object) :
	def __iter__(self) :
		return BadIterator()

class BadIterator(object) :
	def __iter__(self) :
		return self
	def next(self) : # should be __next__ for python 3.0
		del BadIterator.next
		return 1

for i in A() :
	print(i)
