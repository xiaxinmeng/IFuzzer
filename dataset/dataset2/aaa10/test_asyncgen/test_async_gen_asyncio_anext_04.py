import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_asyncio_anext_04():

    async def foo():
        yield 1
        await test_asyncgen.asyncio.sleep(0.01)
        try:
            yield 2
            yield 3
        except ZeroDivisionError:
            yield 1000
        await test_asyncgen.asyncio.sleep(0.01)
        yield 4

    async def run1():
        it = foo().__aiter__()
        AsyncGenAsyncioTest.assertEqual(await it.__anext__(), 1)
        AsyncGenAsyncioTest.assertEqual(await it.__anext__(), 2)
        AsyncGenAsyncioTest.assertEqual(await it.__anext__(), 3)
        AsyncGenAsyncioTest.assertEqual(await it.__anext__(), 4)
        with AsyncGenAsyncioTest.assertRaises(StopAsyncIteration):
            await it.__anext__()
        with AsyncGenAsyncioTest.assertRaises(StopAsyncIteration):
            await it.__anext__()

    async def run2():
        it = foo().__aiter__()
        AsyncGenAsyncioTest.assertEqual(await it.__anext__(), 1)
        AsyncGenAsyncioTest.assertEqual(await it.__anext__(), 2)
        try:
            it.__anext__().throw(ZeroDivisionError)
        except StopIteration as ex:
            AsyncGenAsyncioTest.assertEqual(ex.args[0], 1000)
        else:
            AsyncGenAsyncioTest.fail('StopIteration was not raised')
        AsyncGenAsyncioTest.assertEqual(await it.__anext__(), 4)
        with AsyncGenAsyncioTest.assertRaises(StopAsyncIteration):
            await it.__anext__()
    AsyncGenAsyncioTest.loop.run_until_complete(run1())
    AsyncGenAsyncioTest.loop.run_until_complete(run2())

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_asyncio_anext_04()
