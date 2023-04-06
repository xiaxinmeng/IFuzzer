import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_iteration_01():

    async def gen():
        await test_asyncgen.awaitable()
        a = (yield 123)
        AsyncGenTest.assertIs(a, None)
        await test_asyncgen.awaitable()
        yield 456
        await test_asyncgen.awaitable()
        yield 789
    AsyncGenTest.assertEqual(test_asyncgen.to_list(gen()), [123, 456, 789])

AsyncGenTest = test_asyncgen.AsyncGenTest()

test_async_gen_iteration_01()
