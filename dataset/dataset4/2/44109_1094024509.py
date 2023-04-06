stuff = []
import numpy
def allocator1():
    x = numpy.array([...], dtype='f4')
    stuff.append(x)
    return x.ctypes.data_as(POINTER(c_float))
CFUNCTYPE(POINTER(c_float))(allocator1)