class X:
    def __index__(self):
        b[:] = []
        return 1

b = [1,2,3,4]
b[X()]