@CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
def py_cmp_func(*args):
    (a,b,) = (t[0] for t in args)
    print("py_cmp_func", a, b)
    return a-b