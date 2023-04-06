def __call__(self, *args, **kwargs):
    object = self.__origin__(*args, **kwargs)
    object.__orig_class__ = self
    return object