class X:
    def __index__(self):
        del a[:]
        return 1

a = [0]
a[:X():2]