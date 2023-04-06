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

def test_func_14():

    @types.coroutine
    def gen():
        yield

    async def coro():
        try:
            await gen()
        except GeneratorExit:
            await gen()
    c = coro()
    c.send(None)
    with CoroutineTest.assertRaisesRegex(RuntimeError, 'coroutine ignored GeneratorExit'):
        c.close()

CoroutineTest = test_coroutines.CoroutineTest()
test_func_14()
