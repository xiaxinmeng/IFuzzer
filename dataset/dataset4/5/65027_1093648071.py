import inspect

def get_callable_argspec(fn):
    if inspect.isfunction(fn) or inspect.ismethod(fn):
        inspectable = fn
    elif inspect.isclass(fn):
        inspectable = fn.__init__
    elif hasattr(fn, '__call__'):
        inspectable = fn.__call__
    else:
        inspectable = fn