if sizeof(c_uint) == sizeof(c_void_p):
    c_size_t = c_uint
elif sizeof(c_ulong) == sizeof(c_void_p):
    c_size_t = c_ulong
elif sizeof(c_ulonglong) == sizeof(c_void_p):
    c_size_t = c_ulonglong