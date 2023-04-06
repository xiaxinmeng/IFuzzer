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

def test_comp_5():

    async def f(it):
        for i in it:
            yield i

    async def run_list():
        return [i + 1 for pair in ([10, 20], [30, 40]) if pair[0] > 10 async for i in f(pair) if i > 30]
    CoroutineTest.assertEqual(test_coroutines.run_async(run_list()), ([], [41]))

CoroutineTest = test_coroutines.CoroutineTest()
test_comp_5()
