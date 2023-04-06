import ctypes
class Blah(ctypes.Structure):
    _fields_ = [("a", ctypes.c_uint64, 64),
                ("b", ctypes.c_uint16, 16),
                ("c", ctypes.c_uint8, 8),
                ("d", ctypes.c_uint8, 8)]

x = Blah(0xDEAD,0xBEEF,0x44,0x12)
print(hex(x.a))