def isinstance(inst, cls):
    if type(inst) is cls:
        return True
    if type(cls) is type:
        return type(inst) in cls.mro()
    if type(cls) is tuple:
        for t in cls:
            isinstance(cls, t)
    ...
    raise TypeError