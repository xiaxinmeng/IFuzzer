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

def test_await_15():

    @types.coroutine
    def nop():
        yield

    async def coroutine():
        await nop()

    async def waiter(coro):
        await coro
    coro = coroutine()
    coro.send(None)
    with CoroutineTest.assertRaisesRegex(RuntimeError, 'coroutine is being awaited already'):
        waiter(coro).send(None)

CoroutineTest = test_coroutines.CoroutineTest()
test_await_15()
