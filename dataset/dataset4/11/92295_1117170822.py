
import ctypes
ntdll = ctypes.WinDLL('ntdll')
pmin = ctypes.pointer(ctypes.c_ulong())
pmax = ctypes.pointer(ctypes.c_ulong())
pcur = ctypes.pointer(ctypes.c_ulong())
