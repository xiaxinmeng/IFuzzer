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

def test_func_11():

    async def func():
        pass
    coro = func()
    CoroutineTest.assertIn('__await__', dir(coro))
    CoroutineTest.assertIn('__iter__', dir(coro.__await__()))
    CoroutineTest.assertIn('coroutine_wrapper', repr(coro.__await__()))
    coro.close()

CoroutineTest = test_coroutines.CoroutineTest()
test_func_11()
