class X:
    def __index__(self):
        b[:] = [1, 2, 3]
        return 2

b = [123]*0x1000
b[0:64:X()] = [0]*32