import array

class X:
    def __index__(self):
        del a[:]
        a.append(2)
        return 1

a = array.array("b")
for _ in range(0x10):
    a.append(1)