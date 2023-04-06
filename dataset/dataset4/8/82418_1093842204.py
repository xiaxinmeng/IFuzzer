def sorted(iterable, /, *, key=None, reverse=False):
    """Emulate the built in sorted() function"""
    result = list(iterable)
    result.sort(key=key, reverse=reverse)
    return result