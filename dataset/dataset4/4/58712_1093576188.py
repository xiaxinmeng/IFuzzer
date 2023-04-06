from operator import add
from itertools import izip, starmap

a = b = [1]
for i in xrange(100000):
    a = starmap(add, izip(a, b))

list(a)