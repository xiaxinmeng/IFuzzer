import ctypes
import time

class uint(ctypes.BigEndianStructure):
    _pack_      = 1    # aligned to 8 bits, not ctypes default of 32
    _fields_    = [
                   ("Data0",   ctypes.c_uint, 31),
                   ("Data1",   ctypes.c_uint, 32),
                   ]

class ulonglong(ctypes.BigEndianStructure):
    _pack_      = 1    # aligned to 8 bits, not ctypes default of 32
    _fields_    = [
                   ("Data0",   ctypes.c_ulonglong, 31),
                   ("Data1",   ctypes.c_ulonglong, 32),
                  ]

size_of_structures_in_bytes = 8

def castbytes(type):
    buffer = (ctypes.c_byte * size_of_structures_in_bytes)()
    for index in range(size_of_structures_in_bytes):
        buffer[index] = 0x55
    return ctypes.cast(ctypes.pointer(buffer),
ctypes.POINTER(type)).contents

def print_members(test):
    print("Data0 is 0x%X, Data1 is 0x%X for %s"%(test.Data0, test.Data1,
test.__class__.__name__))

test_classes = [ uint, ulonglong]

Failed = False
tests = [castbytes(type) for type in test_classes]
for test in tests:
    print_members(test)

if not tests[0].Data0 == tests[1].Data0 == 0x2AAAAAAA:
    Failed = True
    print("Data0 failed")
if not tests[0].Data1 == tests[1].Data1 == 0xAAAAAAAA:
    Failed = True
    print("Data1 failed")

if not Failed:
    print("Passed")