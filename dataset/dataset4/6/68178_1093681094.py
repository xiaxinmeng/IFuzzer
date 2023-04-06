def callable(obj):
    return hasattr(type(obj), '__call__')