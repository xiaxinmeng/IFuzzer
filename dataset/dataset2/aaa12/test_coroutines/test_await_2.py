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

def test_await_2():

    async def foo():
        await []
    with CoroutineTest.assertRaisesRegex(TypeError, 'object list can.t.*await'):
        test_coroutines.run_async(foo())

CoroutineTest = test_coroutines.CoroutineTest()
test_await_2()
