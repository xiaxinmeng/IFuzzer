import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_exception_08():

    def sync_gen():
        try:
            yield 1
        finally:
            yield 2
            1 / 0
            yield 3
        yield 100

    async def async_gen():
        try:
            yield 1
            await awaitable()
        finally:
            await awaitable()
            yield 2
            1 / 0
            yield 3
        yield 100
    AsyncGenTest.compare_generators(sync_gen(), async_gen())

AsyncGenTest = test_asyncgen.AsyncGenTest()
test_async_gen_exception_08()
