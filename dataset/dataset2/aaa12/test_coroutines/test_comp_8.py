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

def test_comp_8():

    async def f():
        return [i for i in [1, 2, 3]]
    CoroutineTest.assertEqual(test_coroutines.run_async(f()), ([], [1, 2, 3]))

CoroutineTest = test_coroutines.CoroutineTest()
test_comp_8()
