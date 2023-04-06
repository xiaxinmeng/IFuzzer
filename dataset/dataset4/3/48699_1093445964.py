if not hasattr(lock, 'acquire'):
    raise AttributeError("'%r' has no method 'acquire'" % lock)