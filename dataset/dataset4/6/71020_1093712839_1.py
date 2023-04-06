class CmpRet(c_int):
    pass

cmp_ctype = CFUNCTYPE(CmpRet, POINTER(c_int), POINTER(c_int))

def py_cmp_func(a, b):
    print(a.contents, b.contents)
    return CmpRet(0)