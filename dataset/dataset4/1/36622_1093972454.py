import copy_reg

def pickle_bound_method(method):
    return getattr, (method.im_self, method.__name__)

class _Foo:
    def bar(self):
        pass

_foo = _Foo()

copy_reg.constructor(getattr)
copy_reg.pickle(type(_foo.bar), pickle_bound_method)