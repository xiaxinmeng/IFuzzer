
import logging
from asyncio import sleep, gather, run
from contextlib import asynccontextmanager, contextmanager

@contextmanager
def foo():
    yield


def test():
    f = foo()
    f.__enter__()
    f.__enter__()

test()
