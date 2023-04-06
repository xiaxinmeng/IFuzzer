class myit(list):
    def __bytes__(self): return b'hello'
print (bytes (myit([1,2,3])))
# b'hello'

class mybit(bytes):  # example 
    def __bytes__(self): return b'hello'
print (bytes (mybit(b'a')))
# b'hello'