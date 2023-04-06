import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_iteration_02():

    async def gen():
        await test_asyncgen.awaitable()
        yield 123
        await test_asyncgen.awaitable()
    g = gen()
    ai = g.__aiter__()
    an = ai.__anext__()
    AsyncGenTest.assertEqual(an.__next__(), ('result',))
    try:
        an.__next__()
    except StopIteration as ex:
        AsyncGenTest.assertEqual(ex.args[0], 123)
    else:
        AsyncGenTest.fail('StopIteration was not raised')
    an = ai.__anext__()
    AsyncGenTest.assertEqual(an.__next__(), ('result',))
    try:
        an.__next__()
    except StopAsyncIteration as ex:
        AsyncGenTest.assertFalse(ex.args)
    else:
        AsyncGenTest.fail('StopAsyncIteration was not raised')

AsyncGenTest = test_asyncgen.AsyncGenTest()

test_async_gen_iteration_02()
