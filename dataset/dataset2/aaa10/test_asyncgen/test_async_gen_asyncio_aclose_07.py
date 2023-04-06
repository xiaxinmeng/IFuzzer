import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_asyncio_aclose_07():
    DONE = 0

    async def foo():
        nonlocal DONE
        try:
            yield 1
            1 / 0
        finally:
            await test_asyncgen.asyncio.sleep(0.01)
            await test_asyncgen.asyncio.sleep(0.01)
            DONE += 1
        DONE += 1000

    async def run():
        gen = foo()
        it = gen.__aiter__()
        await it.__anext__()
        await gen.aclose()
    AsyncGenAsyncioTest.loop.run_until_complete(run())
    AsyncGenAsyncioTest.assertEqual(DONE, 1)

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_asyncio_aclose_07()
