import ctypes, struct
libc = ctypes.cdll.msvcrt
buf = ctypes.create_string_buffer(1024)
tm = struct.pack('9i', 2019, 5, 6, 9, 50, 4, 0, 126, 1)
print('count:', libc.strftime(buf, 1024, b'%Z', tm))
print('value:', buf.value)