import array

class X:
    def __index__(self):
        del a[:]
        return 1

a = array.array("b")
a.frombytes(b"A"*0x100)
del a[::X()]