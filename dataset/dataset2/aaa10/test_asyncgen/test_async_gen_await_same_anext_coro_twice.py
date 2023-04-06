import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_await_same_anext_coro_twice():

    async def async_iterate():
        yield 1
        yield 2

    async def run():
        it = async_iterate()
        nxt = it.__anext__()
        await nxt
        with AsyncGenAsyncioTest.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited __anext__\\(\\)/asend\\(\\)'):
            await nxt
        await it.aclose()
    AsyncGenAsyncioTest.loop.run_until_complete(run())

AsyncGenAsyncioTest = test_asyncgen.AsyncGenAsyncioTest()
AsyncGenAsyncioTest.setUp()
test_async_gen_await_same_anext_coro_twice()
