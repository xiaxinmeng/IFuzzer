from test.support import run_with_locale
import collections.abc
from collections import namedtuple
import inspect
import pickle
import locale
import sys
import types
import unittest.mock
import weakref
import typing
import test_types

def test_duck_coro():

    class CoroLike:

        def send(CoroutineTests):
            pass

        def throw(CoroutineTests):
            pass

        def close(CoroutineTests):
            pass

        def __await__(CoroutineTests):
            return CoroutineTests
    coro = CoroLike()

    @types.coroutine
    def foo():
        return coro
    CoroutineTests.assertIs(foo(), coro)
    CoroutineTests.assertIs(foo().__await__(), coro)

CoroutineTests = test_types.CoroutineTests()
test_duck_coro()
