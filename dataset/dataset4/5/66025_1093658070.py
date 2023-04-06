if sys.platform.startswith("aix"):
    if sys.maxsize > 2**32:
        lib = "libc.a(shr_64.o)"
    else:
        lib = "libc.a(shr.o)"
    RTLD_MEMBER = 0x00040000
    lib = ctypes.CDLL(lib, ctypes.DEFAULT_MODE | RTLD_MEMBER)
    _uuid_generate_time = lib.uuid_generate_time
else:
    # The uuid_generate_* routines are provided by libuuid on at least
    # Linux and FreeBSD, and provided by libc on Mac OS X.
    ...