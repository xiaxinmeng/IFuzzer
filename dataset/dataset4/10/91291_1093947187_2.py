def localcontext(ctx=None, **kwargs):
    if ctx is None:
        ctx = decimal.getcontext().copy()
    for key, value in kwargs.items():
        setattr(ctx, key, value)
    return decimal.localcontext(ctx)