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

def test_func_13():

    async def g():
        pass
    coro = g()
    with CoroutineTest.assertRaisesRegex(TypeError, "can't send non-None value to a just-started coroutine"):
        coro.send('spam')
    coro.close()

CoroutineTest = test_coroutines.CoroutineTest()
test_func_13()
