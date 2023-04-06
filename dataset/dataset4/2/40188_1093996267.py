def __get__(self, obj, type=None):
    if obj is None:
        return self
    return partial(self.func, obj, *self.args, **self.kwargs)