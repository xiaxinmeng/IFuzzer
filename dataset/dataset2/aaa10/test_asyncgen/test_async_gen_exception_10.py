import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_exception_10():

    async def gen():
        yield 123
    with AsyncGenTest.assertRaisesRegex(TypeError, 'non-None value .* async generator'):
        gen().__anext__().send(100)

AsyncGenTest = test_asyncgen.AsyncGenTest()

test_async_gen_exception_10()
