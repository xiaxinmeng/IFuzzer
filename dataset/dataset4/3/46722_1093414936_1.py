import ctypes
libc = ctypes.CDLL("libc.so.6")
iconv = libc.iconv_open("ISO-8859-1", "ISO-8859-2")
print(iconv)