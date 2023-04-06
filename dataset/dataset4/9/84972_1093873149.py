from ctypes import c_int, CFUNCTYPE

def func():
    return (1, 2, 3)

cb = CFUNCTYPE(c_int)(func)
cb()