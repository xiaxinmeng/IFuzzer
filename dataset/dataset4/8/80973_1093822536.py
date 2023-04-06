import ctypes, struct
crt_locale = ctypes.CDLL('api-ms-win-crt-locale-l1-1-0', use_errno=True)
crt_time = ctypes.CDLL('api-ms-win-crt-time-l1-1-0', use_errno=True)
crt_locale._wsetlocale.restype = ctypes.c_wchar_p
print('old locale:', crt_locale._wsetlocale(0, 0))
tm = struct.pack('9i', 2019, 5, 6, 9, 50, 4, 0, 126, 1)
wbuf = ctypes.create_unicode_buffer(1024)
print('count:', crt_time.wcsftime(wbuf, 1024, '%Z', tm))
print('value:', wbuf.value)
print('new locale:', crt_locale._wsetlocale(0, 'de_DE'))
print('count:', crt_time.wcsftime(wbuf, 1024, '%Z', tm))
print('value:', wbuf.value)