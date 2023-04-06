
class Index():
    def __index__(self):
        global a
        a.append("2")
        return 999

a = bytearray(b"1")
buf = buffer(a)
s = buf[:1:Index()] 
# buf[Index():x:x] or buf[x:x:Index()] will also crash
