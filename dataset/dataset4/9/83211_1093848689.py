class BitFieldUnion(Union):
    _fields_ = [("a", c_uint32, 16), ("b", c_uint32, 16)]

buff = bytearray(4)

bitfield_union = BitFieldUnion.from_buffer(buff)
bitfield_union.a = 1
bitfield_union.b = 2

print("a is {}".format(bitfield_union.a)) # Prints "a is 1"
print("b is {}".format(bitfield_union.b)) # Prints "b is 2"
print("Buffer: {}".format(buff)) # Prints "Buffer: b'\x01\x00\x00\x00'".