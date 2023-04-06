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

def test_coro_wrapper_send_tuple():

    async def foo():
        return (10,)
    result = test_coroutines.run_async__await__(foo())
    CoroutineTest.assertEqual(result, ([], (10,)))

CoroutineTest = test_coroutines.CoroutineTest()
test_coro_wrapper_send_tuple()
