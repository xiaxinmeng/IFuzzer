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

def test_func_17():

    async def coroutine():
        return 'spam'
    coro = coroutine()
    with CoroutineTest.assertRaisesRegex(StopIteration, 'spam'):
        coro.send(None)
    with CoroutineTest.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        coro.send(None)
    with CoroutineTest.assertRaisesRegex(RuntimeError, 'cannot reuse already awaited coroutine'):
        coro.throw(Exception('wat'))
    coro.close()
    coro.close()

CoroutineTest = test_coroutines.CoroutineTest()
test_func_17()
