def _pass(ns): pass

def new_class(name, bases=(), kwds={}, exec_body=_pass):
    __build_class__(exec_body, name, *bases, **kwds)