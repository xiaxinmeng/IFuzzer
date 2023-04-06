import itertools

p = itertools.product((0,),(0,))
p.__setstate__((0, 1))