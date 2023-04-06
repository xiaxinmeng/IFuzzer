@contextmanager
def optional_cm(cm, *, use_cm=True): # See naming note below
    if cm is None or not use_cm:
        yield
    else:
        with cm:
            yield