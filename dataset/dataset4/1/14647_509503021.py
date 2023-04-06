class S(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_uint8),
        ('b', ctypes.c_uint8, 6),
        ('c', ctypes.c_uint8, 2),
    ]