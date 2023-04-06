f = getattr(func, "__func__", func)
try:
    _overload_registry[f.__module__][f.__qualname__][f.__code__.co_firstlineno] = func
except AttributeError:
    # Not a normal function; ignore.
    pass
return _overload_dummy