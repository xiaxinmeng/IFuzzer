import ctypes
class StructRLimit(ctypes.Structure):
  _fields_ = [('rlim_cur', ctypes.c_ulong), ('rlim_max', ctypes.c_ulong)]
libc = ctypes.cdll.LoadLibrary('libc.so.6')
RLIMIT_NOFILE = 7  # Linux
limits = StructRLimit()
assert libc.getrlimit(RLIMIT_NOFILE, ctypes.byref(limits)) == 0
print(limits.rlim_cur, limits.rlim_max)
limits.rlim_cur = limits.rlim_max
assert libc.setrlimit(RLIMIT_NOFILE, ctypes.byref(limits)) == 0