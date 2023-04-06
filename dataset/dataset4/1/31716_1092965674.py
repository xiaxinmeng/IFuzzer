from functools import partial
_overload_registry = defaultdict(partial(defaultdict, dict))

def new_overload(func):
    f = getattr(func, "__func__", func)
    try:
        _overload_registry[f.__module__][f.__qualname__][f.__code__.co_firstlineno] = func
    except AttributeError:
        raise TypeError("Sorry")
    return _overload_dummy