from _struct import Struct
for i in range(100000):
    L = [Struct.__new__(Struct) for j in range(1000)]
    for s in L:
        try:
            x = s.pack_into(bytearray())
        except SystemError:
            pass
