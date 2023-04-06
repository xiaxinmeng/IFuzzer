class Foo(object):
    def __rdivmod__(self, other):
        return 'rdivmod works'

from fractions import Fraction
a = Fraction(1,1)
b = Foo()
print(divmod(1, b))
print(divmod(a, b))