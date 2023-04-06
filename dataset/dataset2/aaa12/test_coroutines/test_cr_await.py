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

def test_cr_await():

    @types.coroutine
    def a():
        CoroutineTest.assertEqual(inspect.getcoroutinestate(coro_b), inspect.CORO_RUNNING)
        CoroutineTest.assertIsNone(coro_b.cr_await)
        yield
        CoroutineTest.assertEqual(inspect.getcoroutinestate(coro_b), inspect.CORO_RUNNING)
        CoroutineTest.assertIsNone(coro_b.cr_await)

    async def c():
        await a()

    async def b():
        CoroutineTest.assertIsNone(coro_b.cr_await)
        await c()
        CoroutineTest.assertIsNone(coro_b.cr_await)
    coro_b = b()
    CoroutineTest.assertEqual(inspect.getcoroutinestate(coro_b), inspect.CORO_CREATED)
    CoroutineTest.assertIsNone(coro_b.cr_await)
    coro_b.send(None)
    CoroutineTest.assertEqual(inspect.getcoroutinestate(coro_b), inspect.CORO_SUSPENDED)
    CoroutineTest.assertEqual(coro_b.cr_await.cr_await.gi_code.co_name, 'a')
    with CoroutineTest.assertRaises(StopIteration):
        coro_b.send(None)
    CoroutineTest.assertEqual(inspect.getcoroutinestate(coro_b), inspect.CORO_CLOSED)
    CoroutineTest.assertIsNone(coro_b.cr_await)

CoroutineTest = test_coroutines.CoroutineTest()
test_cr_await()
