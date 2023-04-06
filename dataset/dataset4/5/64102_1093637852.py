from collections import namedtuple
from inspect import signature

Point = namedtuple('Point', 'x y')
print(signature(Point.__new__))
# '(_cls, x, y)'
print(signature(Point))
# '(x, y)'