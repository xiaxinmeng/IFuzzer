def __getattr__(self, attr):
    if '__origin__' in self.__dict__ and hasattr(type, attr):
        return getattr(self.__origin__, attr)
    raise AttributeError(attr)