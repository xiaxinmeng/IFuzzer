def join(iterable, sep, *, suffix=None):
    s = sep.join(iterable)
    if s and suffix is not None:
        s += suffix
    return s