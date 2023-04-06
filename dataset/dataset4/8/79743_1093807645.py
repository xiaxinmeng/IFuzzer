from ctypes import c_int
from ctypes import c_double
from ctypes import sizeof
from ctypes import Structure
from struct import Struct

class issueInSizeof(Structure):
    _fields_ = [('KEY',     c_int),                
                ('VALUE',   c_double)]

print(sizeof(issueInSizeof))