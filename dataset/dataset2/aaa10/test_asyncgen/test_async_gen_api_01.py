import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_api_01():

    async def gen():
        yield 123
    g = gen()
    AsyncGenTest.assertEqual(g.__name__, 'gen')
    g.__name__ = '123'
    AsyncGenTest.assertEqual(g.__name__, '123')
    AsyncGenTest.assertIn('.gen', g.__qualname__)
    g.__qualname__ = '123'
    AsyncGenTest.assertEqual(g.__qualname__, '123')
    AsyncGenTest.assertIsNone(g.ag_await)
    AsyncGenTest.assertIsInstance(g.ag_frame, types.FrameType)
    AsyncGenTest.assertFalse(g.ag_running)
    AsyncGenTest.assertIsInstance(g.ag_code, types.CodeType)
    AsyncGenTest.assertTrue(inspect.isawaitable(g.aclose()))

AsyncGenTest = test_asyncgen.AsyncGenTest()

test_async_gen_api_01()
