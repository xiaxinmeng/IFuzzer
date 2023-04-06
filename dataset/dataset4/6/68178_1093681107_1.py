def callable(x):
    return hasattr(x.__class__, '__call__') and hasattr(x, '__call__')