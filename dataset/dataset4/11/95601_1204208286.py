def _insist_future(f, loop):
    f2 = ensure_future(f, loop=loop)
    if f2 is not f:
        warnings.warn("passing non-futures is deprecated")
    return f2