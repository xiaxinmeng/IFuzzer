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

def test_func_1():

    async def foo():
        return 10
    f = foo()
    CoroutineTest.assertIsInstance(f, types.CoroutineType)
    CoroutineTest.assertTrue(bool(foo.__code__.co_flags & inspect.CO_COROUTINE))
    CoroutineTest.assertFalse(bool(foo.__code__.co_flags & inspect.CO_GENERATOR))
    CoroutineTest.assertTrue(bool(f.cr_code.co_flags & inspect.CO_COROUTINE))
    CoroutineTest.assertFalse(bool(f.cr_code.co_flags & inspect.CO_GENERATOR))
    CoroutineTest.assertEqual(test_coroutines.run_async(f), ([], 10))
    CoroutineTest.assertEqual(test_coroutines.run_async__await__(foo()), ([], 10))

    def bar():
        pass
    CoroutineTest.assertFalse(bool(bar.__code__.co_flags & inspect.CO_COROUTINE))

CoroutineTest = test_coroutines.CoroutineTest()
test_func_1()
