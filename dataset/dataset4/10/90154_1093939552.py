
import logging
from contextlib import contextmanager

@contextmanager
def foo():
    yield


def test():
    f = foo()
    f.__enter__()
    f.__enter__()

test()
