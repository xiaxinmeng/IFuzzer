import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_asyncio_01():

    async def gen():
        yield 1
        await test_asyncgen.asyncio.sleep(0.01)
        yield 2
        await test_asyncgen.asyncio.sleep(0.01)
        return
        yield 3
    res = AsyncGenAsyncioTest.loop.run_until_complete(AsyncGenAsyncioTest.to_list(gen()))
    AsyncGenAsyncioTest.assertEqual(res, [1, 2])

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_asyncio_01()
