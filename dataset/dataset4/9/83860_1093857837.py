from functools import singledispatchmethod


def _register(self, cls, method=None):
    if hasattr(cls, "__func__"):
        setattr(cls, "__annotations__", cls.__func__.__annotations__)
    return self.dispatcher.register(cls, func=method)


singledispatchmethod.register = _register