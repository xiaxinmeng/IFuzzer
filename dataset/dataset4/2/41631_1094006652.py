class A(object):
    def __add__(self, other):
        return 'A.__add__', other
class B(A):
    def __radd__(self, other):
        return 'B.__radd__', other