import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_exception_06():

    async def gen():
        yield 123
        raise StopIteration
    with AsyncGenTest.assertRaisesRegex(RuntimeError, 'async generator.*StopIteration'):
        test_asyncgen.to_list(gen())

AsyncGenTest = test_asyncgen.AsyncGenTest()

test_async_gen_exception_06()
