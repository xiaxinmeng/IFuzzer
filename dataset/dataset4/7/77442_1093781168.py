def __getattr__(self, attr):
    return getattr(self.__func__, attr)