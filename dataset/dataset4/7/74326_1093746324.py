class A:
    def __add__(self, other):
        self.log()
        ...
    __radd__ = __add__

class B(A):
    def log(self):
        ...