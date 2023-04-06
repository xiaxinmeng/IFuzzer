class classresolved:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __get__(self, obj, cls):
        try:
            getter = self.wrapped.__get__
        except AttributeError:
            return self.wrapped
        return getter(cls, type(cls))