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

def test_with_13():
    CNT = 0

    class CM:

        async def __aenter__(CoroutineTest):
            1 / 0

        async def __aexit__(CoroutineTest, *e):
            return True

    async def foo():
        nonlocal CNT
        CNT += 1
        async with CM():
            CNT += 1000
        CNT += 10000
    with CoroutineTest.assertRaises(ZeroDivisionError):
        test_coroutines.run_async(foo())
    CoroutineTest.assertEqual(CNT, 1)

CoroutineTest = test_coroutines.CoroutineTest()
test_with_13()
