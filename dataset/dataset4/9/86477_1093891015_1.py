print(ctypes.sizeof(ctypes.c_void_p))
_testdll = ctypes.CDLL(r"TestDll.dll")

def tohex(val, nbits):
	return hex((val + (1 << nbits)) % (1 << nbits))

result = _testdll.GetPointer()
print(tohex(result, 64))
_testdll.SetPointer(result)

result = _testdll.GetPointer1()
print(tohex(result, 64))
_testdll.SetPointer1(result)