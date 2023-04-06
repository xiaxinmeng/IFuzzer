
import ctypes
from ctypes import wintypes
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

INVALID_HANDLE_VALUE = wintypes.HANDLE(-1).value
kernel32.FindFirstFileW.restype = wintypes.HANDLE
kernel32.FindClose.argtypes = (wintypes.HANDLE,)

def get_short_name(path):
    info = wintypes.WIN32_FIND_DATAW()
    h = kernel32.FindFirstFileW(path, ctypes.byref(info))
    if h == INVALID_HANDLE_VALUE:
        raise ctypes.WinError(ctypes.get_last_error())
    kernel32.FindClose(h)
    return info.cAlternateFileName
