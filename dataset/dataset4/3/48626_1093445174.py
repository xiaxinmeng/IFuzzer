import ctypes

class Nested(ctypes.BigEndianStructure):
    _fields_ = (
        ('x', ctypes.c_uint32),
        ('y', ctypes.c_uint32),
    )

class TestStruct(ctypes.BigEndianStructure):
    _fields_ = (
        ('point', Nested),
    )

data = b'\0\0\0\1\0\0\0\2'
assert len(data) == ctypes.sizeof(TestStruct)
obj = ctypes.cast(data, ctypes.POINTER(TestStruct))[0]
assert obj.point.x == 1
assert obj.point.y == 2