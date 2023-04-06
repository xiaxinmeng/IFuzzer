from ctypes import *

class HEADER(BigEndianStructure):
   _fields_ = ( ('pad', c_uint32, 16),
                ('v1', c_uint32, 4),
                ('v2', c_uint32, 12)
              )

b = bytearray(4)
header = HEADER.from_buffer(b)

header.type = 1
assert b == b'\x00\x00\x10\x00'

header.mode = 0x234
assert b == b'\x00\x00\x12\x34'