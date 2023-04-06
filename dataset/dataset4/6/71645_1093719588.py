class A(str):
    pass

class B(str):
    def __radd__(self, other):
        return B(other.uppper() + str(self))

a = A("hello ")
b = B("world")
assert a + b == "HELLO world"