stuff = []
import numpy
def allocator2():
    x = numpy.array([...], dtype='f4')
    stuff.append(x)
    return x
CFUNCTYPE(numpy.ctypeslib.ndpointer('f4'))(allocator2)