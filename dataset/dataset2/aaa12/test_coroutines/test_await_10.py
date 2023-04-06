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

def test_await_10():

    async def baz():
        return 42

    async def bar():
        return baz()

    async def foo():
        return await (await bar())
    CoroutineTest.assertEqual(test_coroutines.run_async(foo()), ([], 42))

CoroutineTest = test_coroutines.CoroutineTest()
test_await_10()
