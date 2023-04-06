import ctypes
def hi():
    class c1(ctypes.Structure):
            _fields_=[('f1',ctypes.c_uint8)]
    class c2(ctypes.Structure):
            _fields_=[('g1',c1*2)]

while True:
    test=hi()