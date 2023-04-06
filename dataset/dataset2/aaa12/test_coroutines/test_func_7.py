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

def test_func_7():

    async def bar():
        return 10
    coro = bar()

    def foo():
        yield from coro
    with CoroutineTest.assertRaisesRegex(TypeError, "cannot 'yield from' a coroutine object in a non-coroutine generator"):
        list(foo())
    coro.close()

CoroutineTest = test_coroutines.CoroutineTest()
test_func_7()
