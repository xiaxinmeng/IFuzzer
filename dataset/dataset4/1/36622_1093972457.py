import copy_reg

def get_method(object, name):
    klass = object.__class__
    fn = klass.__dict__[name]
    return new.instancemethod(fn, object, klass)

def pickle_bound_method(method):
    return get_method, (method.im_self, method.__name__)

class _Foo:
    def bar(self):
        pass

_foo = _Foo()

copy_reg.constructor(get_method)
copy_reg.pickle(type(_foo.bar), pickle_bound_method)