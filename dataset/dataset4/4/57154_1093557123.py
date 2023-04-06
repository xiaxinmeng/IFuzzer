class X(ctypes.Structure):
    _swappedbytes_ = 1
    _pack_ = 1
    _fields_ = [
        ('a', ctypes.c_ubyte, 4),
        ('b', ctypes.c_ubyte, 4),
        ('c', ctypes.c_ushort, 8),
        ('d', ctypes.c_ushort, 8),
    ]