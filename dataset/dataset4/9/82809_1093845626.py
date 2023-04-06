from ctypes import *

libc = CDLL('libc.a(shr_64.o)')


class MemchrArgsHack(Structure):
    _fields_ = [("s", c_char_p), ("c", c_ulong), ("n", c_ulong)]


memchr_args_hack = MemchrArgsHack()
memchr_args_hack.s = b"abcdef"
memchr_args_hack.c = ord('d')
memchr_args_hack.n = 7


class MemchrArgsHack2(Structure):
    _fields_ = [("s", c_char_p), ("c_n", c_ulong * 2)]


memchr_args_hack2 = MemchrArgsHack2()
memchr_args_hack2.s = b"abcdef"
memchr_args_hack2.c_n[0] = ord('d')
memchr_args_hack2.c_n[1] = 7