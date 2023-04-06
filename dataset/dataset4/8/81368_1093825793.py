import ctypes

class Simple(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_uint8),
        ('b', ctypes.c_uint8),
    ]

class Bitfields(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_uint8, 8),
        ('b', ctypes.c_uint8, 8),
    ]

print(Simple.b.size)     # 1
print(Bitfields.b.size)  # 262148