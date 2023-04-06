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

def test_for_2():
    tup = (1, 2, 3)
    refs_before = sys.getrefcount(tup)

    async def foo():
        async for i in tup:
            print('never going to happen')
    with CoroutineTest.assertRaisesRegex(TypeError, "async for' requires an object.*__aiter__.*tuple"):
        test_coroutines.run_async(foo())
    CoroutineTest.assertEqual(sys.getrefcount(tup), refs_before)

CoroutineTest = test_coroutines.CoroutineTest()
test_for_2()
