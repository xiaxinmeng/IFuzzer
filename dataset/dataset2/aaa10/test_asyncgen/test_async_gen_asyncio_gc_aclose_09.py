import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_asyncio_gc_aclose_09():
    DONE = 0

    async def gen():
        nonlocal DONE
        try:
            while True:
                yield 1
        finally:
            await test_asyncgen.asyncio.sleep(0.01)
            await test_asyncgen.asyncio.sleep(0.01)
            DONE = 1

    async def run():
        g = gen()
        await g.__anext__()
        await g.__anext__()
        del g
        await test_asyncgen.asyncio.sleep(0.1)
    AsyncGenAsyncioTest.loop.run_until_complete(run())
    AsyncGenAsyncioTest.assertEqual(DONE, 1)

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_asyncio_gc_aclose_09()
