from __future__ import print_function
import ctypes
class Blah(ctypes.Structure):
    _fields_ = [("a", ctypes.c_uint64, 64),
                ("b", ctypes.c_uint16, 16),
                ("c", ctypes.c_uint8, 8),
                ("d", ctypes.c_uint8, 8)]

x = Blah(0xFEDCBA9876543210,0xBEEF,0x44,0x12)
print(Blah.a, hex(x.a))
print(Blah.b, hex(x.b))
print(Blah.c, hex(x.c))
print(Blah.d, hex(x.d))