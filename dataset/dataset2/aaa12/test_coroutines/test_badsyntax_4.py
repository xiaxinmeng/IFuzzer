import contextlib
import copy
import inspect
import pickle
import sys
import types
import unittest
import warnings
from test import support
from test.support import import_helper
from test.support import warnings_helper
from test.support.script_helper import assert_python_ok
from _testcapi import awaitType as at
from _testcapi import awaitType as at
from _testcapi import awaitType as at
import test_coroutines

def test_badsyntax_4():
    samples = ['def foo(await):\n                async def foo(): pass\n                async def foo():\n                    pass\n                return await + 1\n            ', 'def foo(await):\n                async def foo(): pass\n                async def foo(): pass\n                return await + 1\n            ', 'def foo(await):\n\n                async def foo(): pass\n\n                async def foo(): pass\n\n                return await + 1\n            ', 'def foo(await):\n                """spam"""\n                async def foo():                     pass\n                # 123\n                async def foo(): pass\n                # 456\n                return await + 1\n            ', 'def foo(await):\n                def foo(): pass\n                def foo(): pass\n                async def bar(): return await_\n                await_ = await\n                try:\n                    bar().send(None)\n                except StopIteration as ex:\n                    return ex.args[0] + 1\n            ']
    for code in samples:
        with AsyncBadSyntaxTest.subTest(code=code), AsyncBadSyntaxTest.assertRaises(SyntaxError):
            compile(code, '<test>', 'exec')

AsyncBadSyntaxTest = test_coroutines.AsyncBadSyntaxTest()
test_badsyntax_4()
