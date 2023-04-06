import ctypes
from ctypes import wintypes
path = 'C:\\Python35-64\\vcruntime140.dll'
cfile = ctypes.CDLL(path)
print(cfile._handle)
ctypes.windll.kernel32.FreeLibrary.argtypes = [wintypes.HMODULE]
ctypes.windll.kernel32.FreeLibrary(cfile._handle)