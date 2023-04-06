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

def test_with_9():
    CNT = 0

    class CM:

        async def __aenter__(CoroutineTest):
            return CoroutineTest

        async def __aexit__(CoroutineTest, *e):
            1 / 0

    async def foo():
        nonlocal CNT
        async with CM():
            CNT += 1
    with CoroutineTest.assertRaises(ZeroDivisionError):
        test_coroutines.run_async(foo())
    CoroutineTest.assertEqual(CNT, 1)

CoroutineTest = test_coroutines.CoroutineTest()
test_with_9()
