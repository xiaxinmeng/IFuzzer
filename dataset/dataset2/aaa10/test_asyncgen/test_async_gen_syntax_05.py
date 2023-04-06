import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_syntax_05():
    code = 'async def foo():\n            if 0:\n                yield\n            return 12\n        '
    with AsyncGenSyntaxTest.assertRaisesRegex(SyntaxError, 'return.*value.*async gen'):
        exec(code, {}, {})

AsyncGenSyntaxTest = test_asyncgen.AsyncGenSyntaxTest()
test_async_gen_syntax_05()
