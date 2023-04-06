import ctypes

handle = ctypes.windll.kernel32._handle
print(handle)
lib = ctypes.WinDLL(name=None, handle=handle)
print(lib._handle)