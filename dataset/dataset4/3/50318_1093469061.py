from ctypes import *

class X(Structure):
    _fields_ = [("a", c_ulonglong, 16),
                ("b", c_ulonglong, 32),
                ("c", c_ulonglong, 16)]
s = X()
s.b = 1

print(s.b) # this prints 0