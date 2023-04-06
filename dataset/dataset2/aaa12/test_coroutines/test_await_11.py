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

def test_await_11():

    def ident(val):
        return val

    async def bar():
        return 'spam'

    async def foo():
        return ident(val=await bar())

    async def foo2():
        return (await bar(), 'ham')
    CoroutineTest.assertEqual(test_coroutines.run_async(foo2()), ([], ('spam', 'ham')))

CoroutineTest = test_coroutines.CoroutineTest()
test_await_11()
