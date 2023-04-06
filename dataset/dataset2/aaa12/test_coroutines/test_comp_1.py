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

def test_comp_1():

    async def f(i):
        return i

    async def run_list():
        return [await c for c in [f(1), f(41)]]

    async def run_set():
        return {await c for c in [f(1), f(41)]}

    async def run_dict1():
        return {await c: 'a' for c in [f(1), f(41)]}

    async def run_dict2():
        return {i: await c for (i, c) in enumerate([f(1), f(41)])}
    CoroutineTest.assertEqual(test_coroutines.run_async(run_list()), ([], [1, 41]))
    CoroutineTest.assertEqual(test_coroutines.run_async(run_set()), ([], {1, 41}))
    CoroutineTest.assertEqual(test_coroutines.run_async(run_dict1()), ([], {1: 'a', 41: 'a'}))
    CoroutineTest.assertEqual(test_coroutines.run_async(run_dict2()), ([], {0: 1, 1: 41}))

CoroutineTest = test_coroutines.CoroutineTest()
test_comp_1()
