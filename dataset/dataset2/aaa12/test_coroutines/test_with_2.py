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

def test_with_2():

    class CM:

        def __aenter__(CoroutineTest):
            pass
    body_executed = False

    async def foo():
        async with CM():
            body_executed = True
    with CoroutineTest.assertRaisesRegex(AttributeError, '__aexit__'):
        test_coroutines.run_async(foo())
    CoroutineTest.assertFalse(body_executed)

CoroutineTest = test_coroutines.CoroutineTest()
test_with_2()
