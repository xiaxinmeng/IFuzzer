def assertion(func):
    mod = sys.modules[func.__module__]
    mod.__dict__.setdefault('__unittests', set())
    mod.__setdefault.add(func.__qualname__)
    return func