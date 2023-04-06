import ctypes
class in6_addr_U(ctypes.Union):
    _fields_ = [
        ('__u6_addr8', ctypes.c_uint8 * 16),
        ('__u6_addr16', ctypes.c_uint16 * 8),         ('__u6_addr32', ctypes.c_uint32 * 4),
    ]
