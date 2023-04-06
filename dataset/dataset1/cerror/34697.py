from ctypes import *

class S(Structure):
    _fields_ = [('x', c_int)]

CField = type(S.x)
f = CField()
repr(f) # Crash here
