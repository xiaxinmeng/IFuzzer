class myit(list):
    def __bytes__(self): return b'hello'
print (bytes(b'a'))

class myit(list):
    def __bytes__(self): return b'hello'
print (bytearray (myit([1,2,3])))