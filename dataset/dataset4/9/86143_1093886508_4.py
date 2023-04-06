import os, sys, gc
from ctypes import *

class S(Structure):
    _fields_ = [ ("x", POINTER(c_int)), ("y", POINTER(c_int)) ]

    def __del__(self):
        print("__del__ was called")

def dump_mem(): os.system(f"ps -o rss {os.getpid()}")

dump_mem() # ~ 6 MB

s = S()
s.x = (c_int * 10**8)()
s.y = s.x

dump_mem() # ~ 397 MB

del s # prints "__del__ was called" immediatly

dump_mem() # ~ 397 MB

gc.collect()

dump_mem() # ~ 6 MB