class FT(Structure):
    _fields_ = [("dwLowDateTime", c_ulong, 32),
                ("dwHighDateTime", c_ulong, 32)]


@WINFUNCTYPE(c_void_p, c_int, FT)
def cb(val, ft):
    print(f"callback {val} {ft.dwLowDateTime} {ft.dwHighDateTime}")


lib = WinDLL(r"C:\Temp\CBsimulate\CbClient\CbClient\Debug\DummyCb.dll")

lib.subscribe_cb(cb)

while 1:
    sleep(5)