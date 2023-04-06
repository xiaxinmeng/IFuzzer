import sys
import ctypes
from ctypes.wintypes import HMODULE, LPVOID, LPWSTR, BOOL

# context structure that is used to use regular python functions as callbacks
# where external C code expects C callbacks with a certain signature.
class CallbackContext(ctypes.Structure):
    _fields_ = (
        ("callback", ctypes.py_object),
        ("context", ctypes.py_object),
        )

CallbackContextPtr = ctypes.POINTER(CallbackContext)