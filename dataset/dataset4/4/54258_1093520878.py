from contextlib import contextmanager

CONDITION = False

@contextmanager
def transaction():
    if not CONDITION:
        yield None
    else:
        yield ...

with transaction() as x:
    ...