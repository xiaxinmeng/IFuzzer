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

def test_for_8():
    CNT = 0

    class AI:

        def __aiter__(CoroutineTest):
            1 / 0

    async def foo():
        nonlocal CNT
        async for i in AI():
            CNT += 1
        CNT += 10
    with CoroutineTest.assertRaises(ZeroDivisionError):
        with warnings.catch_warnings():
            warnings.simplefilter('error')
            test_coroutines.run_async(foo())
    CoroutineTest.assertEqual(CNT, 0)

CoroutineTest = test_coroutines.CoroutineTest()
test_for_8()
