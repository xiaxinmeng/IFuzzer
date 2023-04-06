def callable(obj):
    return hasattr(obj, '__call__') or hasattr(obj, '__bases__')

def callable(obj):
    return isinstance(obj, collections.abc.Callable)

def callable(obj):
    return hasattr(obj, '__call__') or type(obj) == types.ClassType

def callable(obj):
    return any("__call__" in klass.__dict__
               for klass in type(obj).__mro__)