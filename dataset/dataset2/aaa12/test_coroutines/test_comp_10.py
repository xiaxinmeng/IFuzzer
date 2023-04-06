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

def test_comp_10():

    async def f():
        xx = {i for i in [1, 2, 3]}
        return {x: x for x in xx}
    CoroutineTest.assertEqual(test_coroutines.run_async(f()), ([], {1: 1, 2: 2, 3: 3}))

CoroutineTest = test_coroutines.CoroutineTest()
test_comp_10()
