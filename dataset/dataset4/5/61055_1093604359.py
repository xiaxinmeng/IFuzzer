def is_bound_method(obj):
    return hasattr(obj, '__self__') and obj.__self__ is not None