import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_asyncio_athrow_tuple():

    async def gen():
        try:
            yield 1
        except ZeroDivisionError:
            yield (2,)

    async def run():
        g = gen()
        v = await g.asend(None)
        AsyncGenAsyncioTest.assertEqual(v, 1)
        v = await g.athrow(ZeroDivisionError)
        AsyncGenAsyncioTest.assertEqual(v, (2,))
        with AsyncGenAsyncioTest.assertRaises(StopAsyncIteration):
            await g.asend(None)
    AsyncGenAsyncioTest.loop.run_until_complete(run())

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_asyncio_athrow_tuple()
