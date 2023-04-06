# With the current functools.py
# WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
#                        '__annotations__', '__defaults__', '__kwdefaults__')

import inspect
import functools
from test import inspect_fodder as mod

@functools.wraps(mod.spam)
def ham(x, y):
    pass

assert ham.__defaults__ == None == inspect.getargspec(ham).defaults 