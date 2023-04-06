import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_asyncio_02():

    async def gen():
        yield 1
        await test_asyncgen.asyncio.sleep(0.01)
        yield 2
        1 / 0
        yield 3
    with AsyncGenAsyncioTest.assertRaises(ZeroDivisionError):
        AsyncGenAsyncioTest.loop.run_until_complete(AsyncGenAsyncioTest.to_list(gen()))

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_asyncio_02()
