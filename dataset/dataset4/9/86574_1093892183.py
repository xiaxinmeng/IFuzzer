from struct import Struct
s = Struct('<2Q500s').pack_into
buffer = bytearray(7000)
data = bytes(300)
s(buffer, 0, 500, 500, memoryview(data)[4:])