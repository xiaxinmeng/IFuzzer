def test():
    from ctypes.wintypes import BOOL, HMODULE, LONG, LPARAM
    import ctypes
    EnumResourceTypes = ctypes.windll.kernel32.EnumResourceTypesA
    EnumResTypeProc = ctypes.WINFUNCTYPE(
        BOOL, HMODULE, LONG, LPARAM)

    resource_types = []
    def callback(hModule, typeid, lParam):
        resource_types.append(typeid)
        return True # keep enumerating

    hModule = None   # Main executable
    RT_MANIFEST = 24 # from winuser.h
    EnumResourceTypes(hModule, EnumResTypeProc(callback), None)