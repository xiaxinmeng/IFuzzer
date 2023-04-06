
import ctypes
import signal

# load debug version of CRT
# comment this line and uncomment one below to load release CRT
crt = getattr(ctypes.cdll, "ucrtbased.dll")
#crt = getattr(ctypes.cdll, "ucrtbase.dll")
f_raise = getattr(crt, "raise")
f_raise.argtypes = [ctypes.c_int]
f_raise.restype = ctypes.c_int
try:
    print("before")
    f_raise(signal.SIGINT)
    print("after - not ok")
except KeyboardInterrupt:
    print("after - ok")
