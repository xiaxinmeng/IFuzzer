@WINFUNCTYPE(c_void_p, c_int, POINTER(FT))
def cb(val, ft):
    print(f"callback {val} {ft.contents}")