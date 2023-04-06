def getattr(obj, attr):
    try:
        return normal_getattr(obj, attr)
    except AttributeError:
        pass
    return obj.__getattr__(attr)