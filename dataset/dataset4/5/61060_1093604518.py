class A(int):
    def __repr__(self):
        raise Exception()
a = A()
d = {a : 1}
repr(d)