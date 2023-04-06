class ClassMethod(object):
    "Emulate PyClassMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        def newfunc(*args, **kwargs):
            return self.f(klass, *args, **kwargs)
        return newfunc
        # "newfunc" emulates "types.MethodType(self.f, klass)"