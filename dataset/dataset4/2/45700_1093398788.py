import ctypes
decode = ctypes.pythonapi.PyUnicodeUCS2_DecodeUnicodeEscape
decode.restype = ctypes.py_object
decode(b'\\1', 1, None)