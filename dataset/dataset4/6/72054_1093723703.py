class X:
    def __index__(self):
        b[:] = []
        return 1

b = bytearray(b"A"*0x1000)
print(b[0:64:X()])