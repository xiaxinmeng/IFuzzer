class A(object):
    def add(self, x, y):
        print(self)
        return x + y
    add10 = partialmethod(add, 10)