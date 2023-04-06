from ctypes import cdll, Structure, c_int, c_void_p, addressof, pointer, POINTER, c_double, byref
clibptr = cdll.LoadLibrary("libpointers.so")

class Effect(Structure):
    _fields_ = [("ptr", POINTER(c_double))]

clibptr.get_effect.restype = POINTER(Effect)
pEffect = clibptr.get_effect()
effect = pEffect.contents
clibptr.print_ptraddress(byref(effect.ptr))