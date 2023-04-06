import ctypes


class X(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ('a', ctypes.c_ubyte, 4),
        ('b', ctypes.c_ubyte, 4),
        ('c', ctypes.c_ushort, 4),
        ('d', ctypes.c_ushort, 12),
    ]