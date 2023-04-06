
class Index(object):
    def __index__(self):
        for c in "foobar"*n:
            a.append(c)
        return n * 4

for n in range(1, 100000, 100):
    a = bytearray("test"*n)
    buf = buffer(a)
    s = buf[:Index():1]
