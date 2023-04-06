@functools.wraps(func)
def wrapper(*args, **kwds):
    w = CoroWrapper(coro(*args, **kwds), func)
    if w._source_traceback:
        del w._source_traceback[-1]
    w.__name__ = func.__name__
    if hasattr(func, '__qualname__'):
        w.__qualname__ = func.__qualname__
    w.__doc__ = func.__doc__
    return w