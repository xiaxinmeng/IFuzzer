
def isgen(g):
    if hasattr(collections.abc, 'Generator'):
        return isinstance(c, collections.abc.Generator)
    else:
        return inspect.isgenerator(g)
