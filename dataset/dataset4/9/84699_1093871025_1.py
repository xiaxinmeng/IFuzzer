def getattr(obj, attr):
    try:
        return normal_getattr(obj, attr)
    except AttributeError:
        return obj.__getattr__(attr)