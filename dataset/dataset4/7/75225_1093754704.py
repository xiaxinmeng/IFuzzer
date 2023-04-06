
import operator

class A:
    def __index__(self): return 0

a = A()
a.__index__ = (lambda self: 1).__get__(a, type(a))
operator.index(a)
