import copy
import types

def copyfunction(func):
    new = types.FunctionType(
            func.__code__,
            func.__globals__,
            func.__name__,
            func.__defaults__,
            func.__closure__
            )
    vars(new).update(vars(func))
    new.__annotations__.update(func.__annotations__)
    if func.__kwdefaults__ is not None:
        new.__kwdefaults__ = func.__kwdefaults__.copy()
    return new