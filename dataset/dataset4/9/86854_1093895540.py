import ctypes

@ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char_p)
def error_handler(fif, message):
    pass