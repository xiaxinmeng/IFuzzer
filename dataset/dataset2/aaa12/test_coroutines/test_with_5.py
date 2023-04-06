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

def test_with_5():

    class CM:

        async def __aenter__(CoroutineTest):
            return CoroutineTest

        async def __aexit__(CoroutineTest, *exc):
            pass

    async def func():
        async with CM():
            assert (1,) == 1
    with CoroutineTest.assertRaises(AssertionError):
        test_coroutines.run_async(func())

CoroutineTest = test_coroutines.CoroutineTest()
test_with_5()
