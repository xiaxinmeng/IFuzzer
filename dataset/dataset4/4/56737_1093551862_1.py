class MyStructure(ctypes.BigEndianStructure):
    _pack_      = 1    # aligned to 8 bits, not ctypes default of 32
    _fields_    = [
                   ("Data0",   ctypes.c_uint32, 32),
                   ("Data1",   ctypes.c_uint8, 3),
                   ("Data2",   ctypes.c_uint16, 12),
                  ]