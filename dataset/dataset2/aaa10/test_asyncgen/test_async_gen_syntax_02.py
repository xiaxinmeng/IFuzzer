import inspect
import types
import unittest
from test.support.import_helper import import_module
import test_asyncgen

def test_async_gen_syntax_02():
    code = 'async def foo():\n            yield from 123\n        '
    with AsyncGenSyntaxTest.assertRaisesRegex(SyntaxError, 'yield from.*inside async'):
        exec(code, {}, {})

AsyncGenSyntaxTest = test_asyncgen.AsyncGenSyntaxTest()
test_async_gen_syntax_02()
