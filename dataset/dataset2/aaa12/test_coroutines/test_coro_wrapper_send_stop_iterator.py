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

def test_coro_wrapper_send_stop_iterator():

    async def foo():
        return StopIteration(10)
    result = test_coroutines.run_async__await__(foo())
    CoroutineTest.assertIsInstance(result[1], StopIteration)
    CoroutineTest.assertEqual(result[1].value, 10)

CoroutineTest = test_coroutines.CoroutineTest()
test_coro_wrapper_send_stop_iterator()
