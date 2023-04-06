class X:
    def __index__(self):
        del b[0:0x10000]
        return 1
        
b = bytearray(b"A"*0x10000)
b[0:0x8000:X()] = bytearray(b"B"*0x8000)