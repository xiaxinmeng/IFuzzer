import ctypes
import binascii

class BitField1(ctypes.BigEndianStructure):
    _pack_ = 1
    _fields_ = [
    ('a', ctypes.c_uint, 3),
    ('b', ctypes.c_uint, 1),
    ]

class BitField1U(ctypes.Union):
    _pack_ = 1
    _fields_ = [("fields", BitField1), 
        ("raw_bytes", ctypes.c_ubyte * 4)]

class BitField2(ctypes.BigEndianStructure):
    _pack_ = 1
    _fields_ = [
    ('a', ctypes.c_ushort, 3),
    ('b', ctypes.c_ushort, 1),
    ]

class BitField2U(ctypes.Union):
    _pack_ = 1
    _fields_ = [("fields", BitField2), 
        ("raw_bytes", ctypes.c_ubyte * 4)]

def printBytes(raw_bytes) :
    ba = bytearray(raw_bytes)
    print(binascii.hexlify(ba))
    
def printFields(fields) :
    print(fields.a),
    print(fields.b),
    print

b1 = BitField1U()
b2 = BitField2U()