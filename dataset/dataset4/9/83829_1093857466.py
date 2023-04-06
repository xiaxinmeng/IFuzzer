from math import gcd as GCD
from functools import reduce
from itertools import starmap, chain

def gcd(*args):
    return reduce(GCD, args, 0)

iterables = [[10, 20, 30],
             [],
             [0, 0, 0],
             [5],
             [-15, -10000000]]

a = gcd(*chain.from_iterable(iterables))
b = gcd(*starmap(gcd, iterables))
assert a == b == 5