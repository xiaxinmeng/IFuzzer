import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_asyncio_aclose_06():

    async def foo():
        try:
            yield 1
            1 / 0
        finally:
            await test_asyncgen.asyncio.sleep(0.01)
            yield 12

    async def run():
        gen = foo()
        it = gen.__aiter__()
        await it.__anext__()
        await gen.aclose()
    with AsyncGenAsyncioTest.assertRaisesRegex(RuntimeError, 'async generator ignored GeneratorExit'):
        AsyncGenAsyncioTest.loop.run_until_complete(run())

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_asyncio_aclose_06()
