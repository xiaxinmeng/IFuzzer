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

def test_copy():

    async def func():
        pass
    coro = func()
    with CoroutineTest.assertRaises(TypeError):
        copy.copy(coro)
    aw = coro.__await__()
    try:
        with CoroutineTest.assertRaises(TypeError):
            copy.copy(aw)
    finally:
        aw.close()

CoroutineTest = test_coroutines.CoroutineTest()
test_copy()
