import ctypes as ct

class U(ct.Union):
    _pack_=True
    _fields_=[
        ('a', ct.c_int),
        ('b', ct.c_int),
    ]

class S(ct.BigEndianStructure):
    _pack_=True
    _fields_=[
        ('x', ct.c_int),
        ('y', U),
    ]