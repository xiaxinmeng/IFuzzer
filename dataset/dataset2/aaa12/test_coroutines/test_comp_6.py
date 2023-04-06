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

def test_comp_6():

    async def f(it):
        for i in it:
            yield i

    async def run_list():
        return [i + 1 async for seq in f([(10, 20), (30,)]) for i in seq]
    CoroutineTest.assertEqual(test_coroutines.run_async(run_list()), ([], [11, 21, 31]))

CoroutineTest = test_coroutines.CoroutineTest()
test_comp_6()
