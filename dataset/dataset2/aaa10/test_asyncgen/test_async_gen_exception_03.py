import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_exception_03():

    async def gen():
        await test_asyncgen.awaitable()
        yield 123
        await test_asyncgen.awaitable(throw=True)
        yield 456
    with AsyncGenTest.assertRaises(test_asyncgen.AwaitException):
        test_asyncgen.to_list(gen())

AsyncGenTest = test_asyncgen.AsyncGenTest()

test_async_gen_exception_03()
