import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_asyncio_03():
    loop = AsyncGenAsyncioTest.loop

    class Gen:

        async def __aiter__(AsyncGenAsyncioTest):
            yield 1
            await test_asyncgen.asyncio.sleep(0.01)
            yield 2
    res = loop.run_until_complete(AsyncGenAsyncioTest.to_list(Gen()))
    AsyncGenAsyncioTest.assertEqual(res, [1, 2])

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_asyncio_03()
