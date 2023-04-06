import ctypes

for field_width in range(32, 1, -1):
    class TestStruct(ctypes.Structure):
        _fields_ = [
            ("Field1", ctypes.c_uint32, field_width),
            ("Field2", ctypes.c_uint8, 8)
        ]

    cmd = TestStruct()
    cmd.Field2 = 1
    if cmd.Field2 != 1:
        raise RuntimeError(f"{field_width=}, {cmd.Field2=} != 1")

print("All good")