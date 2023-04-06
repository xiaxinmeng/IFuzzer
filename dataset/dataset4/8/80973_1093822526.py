import ctypes, struct
libc = ctypes.cdll.msvcrt
buf = ctypes.create_string_buffer(1024)
tm = struct.pack('9i', 2019, 5, 6, 9, 50, 4, 0, 126, 1)
print('count:', libc.strftime(buf, 1024, b'%Z', tm))
print('value:', buf.value)
wbuf = ctypes.create_unicode_buffer(1024)
print('count:', libc.wcsftime(wbuf, 1024, '%Z', tm))
print('value:', wbuf.value)
print('count:', libc.mbstowcs(wbuf, buf, 1024))
print('value:', wbuf.value)