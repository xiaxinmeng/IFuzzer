class Obj:
    pass

obj = Obj(); obj.foo = bar  # usually used
jbo = functools.partial(Obj, foo=bar)