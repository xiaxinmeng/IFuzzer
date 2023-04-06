def get_method(object, name):
    klass = object.__class__
    fn = getattr(klass, name)
    return new.instancemethod(fn, object, klass)