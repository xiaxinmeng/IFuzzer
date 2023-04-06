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

def test_with_6():

    class CM:

        def __aenter__(CoroutineTest):
            return 123

        def __aexit__(CoroutineTest, *e):
            return 456

    async def foo():
        async with CM():
            pass
    with CoroutineTest.assertRaisesRegex(TypeError, "'async with' received an object from __aenter__ that does not implement __await__: int"):
        test_coroutines.run_async(foo())

CoroutineTest = test_coroutines.CoroutineTest()
test_with_6()
