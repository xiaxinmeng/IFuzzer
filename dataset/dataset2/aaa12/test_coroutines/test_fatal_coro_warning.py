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

def test_fatal_coro_warning():

    async def func():
        pass
    with warnings.catch_warnings(), support.catch_unraisable_exception() as cm:
        warnings.filterwarnings('error')
        coro = func()
        coro_repr = repr(coro)
        coro = None
        support.gc_collect()
        CoroutineTest.assertIn('was never awaited', str(cm.unraisable.exc_value))
        CoroutineTest.assertEqual(repr(cm.unraisable.object), coro_repr)

CoroutineTest = test_coroutines.CoroutineTest()
test_fatal_coro_warning()
