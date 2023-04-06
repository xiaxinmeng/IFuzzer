from ctypes import *

libc = CDLL('/usr/lib64/libc-2.31.so')

class MemchrArgsHack(Structure):
    _fields_ = [("s", c_char_p), ("c", c_uint), ("n", c_uint)]

memchr_args_hack = MemchrArgsHack()
memchr_args_hack.s = b"abcdef"
memchr_args_hack.c = ord('d')
memchr_args_hack.n = 7

class MemchrArgsHack2(Structure):
    _fields_ = [("s", c_char_p), ("c_n", c_uint * 2)]

memchr_args_hack2 = MemchrArgsHack2()
memchr_args_hack2.s = b"abcdef"
memchr_args_hack2.c_n[0] = ord('d')
memchr_args_hack2.c_n[1] = 7