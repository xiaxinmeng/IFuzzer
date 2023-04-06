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

def test_await_12():

    async def coro():
        return 'spam'
    c = coro()

    class Awaitable:

        def __await__(CoroutineTest):
            return c

    async def foo():
        return await Awaitable()
    with CoroutineTest.assertRaisesRegex(TypeError, '__await__\\(\\) returned a coroutine'):
        test_coroutines.run_async(foo())
    c.close()

CoroutineTest = test_coroutines.CoroutineTest()
test_await_12()
