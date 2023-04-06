import ctypes, pickle

class MyStruct(ctypes.Structure):
  _fields_ = [('name', ctypes.c_wchar*2)]

s = MyStruct('DC')

pickle.dumps(s) # raises ValueError.