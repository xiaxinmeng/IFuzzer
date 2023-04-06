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

def test_comp_7():

    async def f():
        yield 1
        yield 2
        raise Exception('aaa')

    async def run_list():
        return [i async for i in f()]
    with CoroutineTest.assertRaisesRegex(Exception, 'aaa'):
        test_coroutines.run_async(run_list())

CoroutineTest = test_coroutines.CoroutineTest()
test_comp_7()
