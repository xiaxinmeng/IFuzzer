class X:
    def __index__(self):
        b[:] = []
        return 1

b = [1]
b.index(1, X())