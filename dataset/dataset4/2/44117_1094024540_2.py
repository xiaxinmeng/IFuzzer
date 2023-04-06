func = CDLL(_ctypes_test.__file__)._testfunc_p_p
func.restype = c_void_p
func.argtypes = [ndpointer(dtype=numpy.float64)]