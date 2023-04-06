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

def test_func_6():

    @types.coroutine
    def bar():
        yield 1
        yield 2

    async def foo():
        await bar()
    f = foo()
    CoroutineTest.assertEqual(f.send(None), 1)
    CoroutineTest.assertEqual(f.send(None), 2)
    with CoroutineTest.assertRaises(StopIteration):
        f.send(None)

CoroutineTest = test_coroutines.CoroutineTest()
test_func_6()
