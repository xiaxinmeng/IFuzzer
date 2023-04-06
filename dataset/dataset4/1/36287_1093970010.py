r = repr(some_double)
if 'n' in r or 'N' in r:
    raise ValueError(...)