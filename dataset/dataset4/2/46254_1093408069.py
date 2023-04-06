from ctypes import *

class AutoStrParam(c_char_p):
    @classmethod
    def from_param(cls, value):
        return str(value)

strlen = cdll.LoadLibrary('msvcrt').strlen
strlen.argtypes = [AutoStrParam]