from ctypes import *

cdll.LoadLibrary("libc.so.7")
libc = CDLL("libc.so.7")