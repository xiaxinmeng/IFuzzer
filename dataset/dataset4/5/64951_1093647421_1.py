@contextlib.contextmanager
def mp(ob, attr, new):
    old = getattr(ob, attr)
    setattr(ob, attr, new)
    yield
    setattr(ob, attr, old)