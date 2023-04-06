import sys
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

print(fun())

sys.getrefcount(None)

print(fun())

sys.getrefcount(None)

print(fun())

sys.getrefcount(None)

while True:
    fun()
