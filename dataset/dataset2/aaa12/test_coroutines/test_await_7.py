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

def test_await_7():

    class Awaitable:

        def __await__(CoroutineTest):
            yield 42
            return 100

    async def foo():
        return await Awaitable()
    CoroutineTest.assertEqual(test_coroutines.run_async(foo()), ([42], 100))

CoroutineTest = test_coroutines.CoroutineTest()
test_await_7()
