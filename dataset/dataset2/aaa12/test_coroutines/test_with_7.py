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

def test_with_7():

    class CM:

        async def __aenter__(CoroutineTest):
            return CoroutineTest

        def __aexit__(CoroutineTest, *e):
            return 444

    async def foo():
        async with CM():
            1 / 0
    try:
        test_coroutines.run_async(foo())
    except TypeError as exc:
        CoroutineTest.assertRegex(exc.args[0], "'async with' received an object from __aexit__ that does not implement __await__: int")
        CoroutineTest.assertTrue(exc.__context__ is not None)
        CoroutineTest.assertTrue(isinstance(exc.__context__, ZeroDivisionError))
    else:
        CoroutineTest.fail('invalid asynchronous context manager did not fail')

CoroutineTest = test_coroutines.CoroutineTest()
test_with_7()
