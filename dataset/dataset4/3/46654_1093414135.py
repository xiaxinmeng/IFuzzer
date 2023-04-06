def silence_py3k(func):
    def decorator(*args, **kwargs):
        warnings.simplefilter("ignore", warnings.DeprecationWarning)
        func(*args, **kwargs)
        warnings.simplefilter("default", warnings.DeprecationWarning)
    if sys.flags_py3kwarning:
        return decorator
    else:
        return func