def __call__(self, *args, **kwargs):
    object = self.__origin__.__new__(*args, **kwargs)
    object.__orig_class__ = self
    object.__init__(*args, **kwargs)
    return object