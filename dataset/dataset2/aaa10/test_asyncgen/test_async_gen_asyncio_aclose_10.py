import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_asyncio_aclose_10():
    DONE = 0

    def foo():
        try:
            yield
        except:
            pass
    g = foo()
    g.send(None)
    g.close()

    async def gen():
        nonlocal DONE
        try:
            yield
        except:
            pass
        DONE = 1

    async def run():
        nonlocal DONE
        g = gen()
        await g.asend(None)
        await g.aclose()
        DONE += 10
    AsyncGenAsyncioTest.loop.run_until_complete(run())
    AsyncGenAsyncioTest.assertEqual(DONE, 11)

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_asyncio_aclose_10()
