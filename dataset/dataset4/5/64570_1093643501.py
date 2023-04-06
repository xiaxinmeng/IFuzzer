def replace(self, *args, **kwargs):
    sig = inspect.signature(self.__new__)
    bound = sig.bind_partial(type(self), *args, **kwargs)
    for arg in sig.parameters:
        if arg not in bound.arguments:
            bound.arguments[arg] = getattr(self, arg)
    return self.__new__(*bound.args, **bound.kwargs)