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

def test_for_3():

    class I:

        def __aiter__(CoroutineTest):
            return CoroutineTest
    aiter = I()
    refs_before = sys.getrefcount(aiter)

    async def foo():
        async for i in aiter:
            print('never going to happen')
    with CoroutineTest.assertRaisesRegex(TypeError, 'that does not implement __anext__'):
        test_coroutines.run_async(foo())
    CoroutineTest.assertEqual(sys.getrefcount(aiter), refs_before)

CoroutineTest = test_coroutines.CoroutineTest()
test_for_3()
