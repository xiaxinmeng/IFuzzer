import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_aclose_twice_with_different_coros():

    async def async_iterate():
        yield 1
        yield 2

    async def run():
        it = async_iterate()
        await it.aclose()
        await it.aclose()
    AsyncGenAsyncioTest.loop.run_until_complete(run())

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_aclose_twice_with_different_coros()
