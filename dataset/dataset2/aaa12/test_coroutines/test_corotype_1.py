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

def test_corotype_1():
    ct = types.CoroutineType
    CoroutineTest.assertIn('into coroutine', ct.send.__doc__)
    CoroutineTest.assertIn('inside coroutine', ct.close.__doc__)
    CoroutineTest.assertIn('in coroutine', ct.throw.__doc__)
    CoroutineTest.assertIn('of the coroutine', ct.__dict__['__name__'].__doc__)
    CoroutineTest.assertIn('of the coroutine', ct.__dict__['__qualname__'].__doc__)
    CoroutineTest.assertEqual(ct.__name__, 'coroutine')

    async def f():
        pass
    c = f()
    CoroutineTest.assertIn('coroutine object', repr(c))
    c.close()

CoroutineTest = test_coroutines.CoroutineTest()
test_corotype_1()
