import ctypes
import time

class closest_fit(ctypes.BigEndianStructure):
#    _pack_      = 1    # aligned to 8 bits, not ctypes default of 32
    _fields_    = [
                   ("Data0",   ctypes.c_ubyte, 7),
                   ("Data1",   ctypes.c_ubyte, 8),
                   ]

class all_ulong(ctypes.BigEndianStructure):
#    _pack_      = 1    # aligned to 8 bits, not ctypes default of 32
    _fields_    = [
                   ("Data0",   ctypes.c_ulonglong, 7),
                   ("Data1",   ctypes.c_ulonglong, 8),
                  ]

def castbytes(type):
    buffer = (ctypes.c_byte * 2)()
    buffer[0] = 0x55
    buffer[1] = 0x55
    return ctypes.cast(ctypes.pointer(buffer),
ctypes.POINTER(type)).contents

def print_members(test):
    print("Data0 is 0x%X, Data1 is 0x%X for %s"%(test.Data0, test.Data1,
test.__class__.__name__))

test_classes = [ closest_fit, all_ulonglong]

Failed = False
tests = [castbytes(type) for type in test_classes]
for test in tests:
    print_members(test)
    if not tests[0].Data0 == tests[1].Data0: 
        Failed = True
    if not tests[0].Data1 == tests[1].Data1: 
        Failed = True

if Failed:
    print("Failed")
else:
    print("Passed")