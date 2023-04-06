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

def test_func_9():

    async def foo():
        pass
    with CoroutineTest.assertWarnsRegex(RuntimeWarning, "coroutine '.*test_func_9.*foo' was never awaited"):
        foo()
        support.gc_collect()
    with CoroutineTest.assertWarnsRegex(RuntimeWarning, "coroutine '.*test_func_9.*foo' was never awaited"):
        with CoroutineTest.assertRaises(TypeError):
            for _ in foo():
                pass
        support.gc_collect()

CoroutineTest = test_coroutines.CoroutineTest()
test_func_9()
