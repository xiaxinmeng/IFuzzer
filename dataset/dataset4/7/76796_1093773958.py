import builtins
class K(dict):
    def __getitem__(self, k):
            if k not in builtins.__dict__:
                    print("get %s" % k)
            return dict.__getitem__(self, k)
    def __setitem__(self, k, v):
            print("set %s" % k)
            dict.__setitem__(self, k, v)
exec("""
foo = "bar"
foo
try:
    qyz
except NameError:
    pass
class K:
    baz = foo
    def f(ggg=foo): pass
def g(ggg=foo):
    global f
    f = 87
    f
g()
""", K())