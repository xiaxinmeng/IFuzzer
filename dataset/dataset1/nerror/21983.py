import ctypes
class Struct(ctypes.Structure):
    _fields_ = [('a', ctypes.c_uint32)] 
s = '0'*100
ctypes.cast(s,Struct)
