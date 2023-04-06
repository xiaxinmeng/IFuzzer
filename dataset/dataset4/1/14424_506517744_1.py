import ctypes
ntdll = ctypes.WinDLL('ntdll')

if hasattr(ntdll, 'RtlAreLongPathsEnabled'):

    ntdll.RtlAreLongPathsEnabled.restype = ctypes.c_ubyte
    ntdll.RtlAreLongPathsEnabled.argtypes = ()

    def are_long_paths_enabled():
        return bool(ntdll.RtlAreLongPathsEnabled())

else:

    def are_long_paths_enabled():
        return False