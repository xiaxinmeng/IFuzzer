from collections import Iterator
a = A()
isinstance(a, Iterator) # True
next(a) # TypeError: 'int' object is not callable