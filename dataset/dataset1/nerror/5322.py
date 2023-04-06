class A(object):
    def __new__(self):
        raise TypeError('i do not exist')
class B(A):
    __new__ = object.__new__
    def __init__(self, x):
        self.x = x
B(1)
