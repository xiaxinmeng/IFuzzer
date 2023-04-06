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

def test_for_11():

    class F:

        def __aiter__(CoroutineTest):
            return CoroutineTest

        def __anext__(CoroutineTest):
            return CoroutineTest

        def __await__(CoroutineTest):
            1 / 0

    async def main():
        async for _ in F():
            pass
    with CoroutineTest.assertRaisesRegex(TypeError, 'an invalid object from __anext__') as c:
        main().send(None)
    err = c.exception
    CoroutineTest.assertIsInstance(err.__cause__, ZeroDivisionError)

CoroutineTest = test_coroutines.CoroutineTest()
test_for_11()
