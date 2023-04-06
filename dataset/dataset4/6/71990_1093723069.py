from ctypes import *
from ctypes.wintypes import *

class CustomPHKEY(object):
    def __init__(self, value):
        self._as_parameter_ = HKEY(value)

function = windll.function
function.argtypes = [POINTER(HKEY)]
function.restype = LONG
result = CustomPHKEY(0)
function(result)