def serialized(lock):
    def _serialized(func):
        def __serialized(*args, **kwds):
            with lock:
                return func(*args, **kwds)
        __serialized.__doc__ = func.__doc__
        return __serialized
    return _serialized