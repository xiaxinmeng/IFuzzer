import ctypes, sys 
names = """
PyRun_String
PyRun_AnyFile
PyRun_AnyFileEx
PyRun_AnyFileFlags
PyRun_SimpleString
PyRun_SimpleFile
PyRun_SimpleFileEx
PyRun_InteractiveOne
PyRun_InteractiveLoop
PyRun_File
PyRun_FileEx
PyRun_FileFlags
"""
api = ctypes.pythonapi
api2 = ctypes.PyDLL("", handle=sys.dllhandle)
for name in names.split():
    if not hasattr(api, name) or not hasattr(api2, name):
        print("MISSING NAME", name)