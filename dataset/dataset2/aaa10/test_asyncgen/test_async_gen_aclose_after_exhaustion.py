import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_aclose_after_exhaustion():

    async def async_iterate():
        yield 1
        yield 2

    async def run():
        it = async_iterate()
        async for _ in it:
            pass
        await it.aclose()
    AsyncGenAsyncioTest.loop.run_until_complete(run())

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_aclose_after_exhaustion()
