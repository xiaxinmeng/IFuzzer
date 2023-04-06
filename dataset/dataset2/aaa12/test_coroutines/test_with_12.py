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

def test_with_12():
    CNT = 0

    class CM:

        async def __aenter__(CoroutineTest):
            return CoroutineTest

        async def __aexit__(CoroutineTest, *e):
            return True

    async def foo():
        nonlocal CNT
        async with CM() as cm:
            CoroutineTest.assertIs(cm.__class__, CM)
            raise RuntimeError
    test_coroutines.run_async(foo())

CoroutineTest = test_coroutines.CoroutineTest()
test_with_12()
