# The uuid_generate_* routines are provided by libuuid on at least
# Linux and FreeBSD, and provided by libc on Mac OS X.
if sys.platform == "darwin":
    libname = "libc.dylib"
else:
    libname = "libuuid.so.1"
_ctypes_lib = ctypes.CDLL(libname)