class metaclass(type):
    def __getattribute__(self, name):
        if name in ["__reduce__", "__getstate__", 
"__setstate__"]:
            return lambda s=self, f=getattr(type(self), 
name): f(s)
        return type.__getattribute__(self, name)