from operator import add
from itertools import starmap

a = b = [1]
for i in range(100000):
    a = starmap(add, zip(a, b))

list(a)