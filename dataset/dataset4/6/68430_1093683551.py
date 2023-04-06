class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value

from timeit import timeit
a = A(1, 2)
timeit('a.x', 'from __main__ import a')
timeit('a.y', 'from __main__ import a')