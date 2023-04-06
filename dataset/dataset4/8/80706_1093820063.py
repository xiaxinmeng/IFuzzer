import types
import sys

class MyInt:
    def __index__(self):
        return SOMEINTEGER

if sys.version_info[0] == 2:
    from future_builtins import hex, oct
    MyInt.__hex__ = types.MethodType(hex, None, MyInt)
    MyInt.__oct__ = types.MethodType(oct, None, MyInt)
    del hex, oct