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

def test_func_15():

    async def spammer():
        return 'spam'

    async def reader(coro):
        return await coro
    spammer_coro = spammer()
    with CoroutineTest.assertRaisesRegex(StopIteration, 'spam'):
        reader(spammer_coro).send(None)
    with CoroutineTest.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        reader(spammer_coro).send(None)

CoroutineTest = test_coroutines.CoroutineTest()
test_func_15()
