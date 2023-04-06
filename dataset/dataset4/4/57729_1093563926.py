import pickle, copyreg, operator, sys, pickletools, types

class AttrGetter(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):                 # pretend to be callable
        raise RuntimeError
    def __reduce__(self):
        return operator.attrgetter, (self.name,)

def reduce_by_qualname(obj):
    mod = sys.modules[obj.__module__]
    first, rest = obj.__qualname__.split('.', 1)
    firstobj = getattr(mod, first)
    assert operator.attrgetter(rest)(firstobj) is obj
    return AttrGetter(rest), (firstobj,)

# FunctionType defaults to save_global but uses fallback if it fails
copyreg.pickle(types.FunctionType, reduce_by_qualname)

class A(object):
    class B(object):
        class C(object):
            @staticmethod
            def foo():
                print("foo foo foo")

def bar():
    print("bar bar bar")

for obj in [A.B.C.foo, bar]:
    data = pickle.dumps(obj, 2)
    pickletools.dis(data)
    func = pickle.loads(data)
    assert func is obj
    func()