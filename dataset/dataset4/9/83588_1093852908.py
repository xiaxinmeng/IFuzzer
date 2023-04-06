class BitFieldStruct(ctypes.LittleEndianStructure):
    _fields_ = [
        ("long_field", C_UINT32, 29),
        ("short_field_0", C_UINT8, 1),
        ("short_field_1", C_UINT8, 1),
        ("short_field_2", C_UINT8, 1),
    ]


class BitField(ctypes.Union):
    _anonymous_ = ("fields",)
    _fields_ = [
        ("fields", BitFieldStruct),
        ("as32bit", C_UINT32)
    ]

def test_bit_field_union():
    f = BitField()
    f.as32bit = int.from_bytes([255, 255, 255, 255], byteorder='little')