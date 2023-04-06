import ctypes
pstring = ctypes.windll.kernel32.GetCommandLineW ()
print (ctypes.c_wchar_p (pstring).value)