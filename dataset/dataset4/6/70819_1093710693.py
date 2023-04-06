def public(thing=None, **kws):
    mdict = (sys._getframe(1).f_globals
             if thing is None
             else sys.modules[thing.__module__].__dict__)
    dunder_all = mdict.setdefault('__all__', [])
    if thing is not None:
        dunder_all.append(thing.__name__)
    for key, value in kws.items():
        dunder_all.append(key)
        mdict[key] = value
    return thing