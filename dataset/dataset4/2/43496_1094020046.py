def compose(f, g):
    return lambda *args, **kws: f(g(*args, **kws))