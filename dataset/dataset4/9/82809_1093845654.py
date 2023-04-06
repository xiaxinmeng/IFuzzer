from ctypes import *

mine = CDLL('./MemchrArgsHack2.so')

class MemchrArgsHack2(Structure):
    _fields_ = [("s",   c_char_p),
                ("c_n", c_ulong * 2)]

memchr_args_hack2 = MemchrArgsHack2()
memchr_args_hack2.s = b"abcdef"
memchr_args_hack2.c_n[0] = ord('d')
memchr_args_hack2.c_n[1] = 7