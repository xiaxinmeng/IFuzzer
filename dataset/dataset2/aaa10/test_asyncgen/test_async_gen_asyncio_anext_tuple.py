import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_asyncio_anext_tuple():

    async def foo():
        try:
            yield (1,)
        except ZeroDivisionError:
            yield (2,)

    async def run():
        it = foo().__aiter__()
        AsyncGenAsyncioTest.assertEqual(await it.__anext__(), (1,))
        with AsyncGenAsyncioTest.assertRaises(StopIteration) as cm:
            it.__anext__().throw(ZeroDivisionError)
        AsyncGenAsyncioTest.assertEqual(cm.exception.args[0], (2,))
        with AsyncGenAsyncioTest.assertRaises(StopAsyncIteration):
            await it.__anext__()
    AsyncGenAsyncioTest.loop.run_until_complete(run())

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_asyncio_anext_tuple()
