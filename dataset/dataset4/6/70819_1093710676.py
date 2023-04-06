import sys

def public(thing):
    if isinstance(thing, str):
        mdict = sys._getframe(1).f_globals
        name = thing
    else:
        mdict = sys.modules[thing.__module__].__dict__
        name = thing.__name__
    dunder_all = mdict.setdefault('__all__', [])
    dunder_all.append(name)
    return thing