_all = all
def all(obj):
    if isinstance(obj, range):
        return 0 not in obj
    return _all(obj)