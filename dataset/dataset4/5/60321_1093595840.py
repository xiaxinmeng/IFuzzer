class Int(ctypes.Structure):
           _fields_ = [ ("_i", ctypes.c_uint64),
                                   ("undef", ctypes.c_bool)]