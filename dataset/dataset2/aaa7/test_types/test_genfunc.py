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

def test_genfunc():

    def gen():
        yield
    CoroutineTests.assertIs(types.coroutine(gen), gen)
    CoroutineTests.assertIs(types.coroutine(types.coroutine(gen)), gen)
    CoroutineTests.assertTrue(gen.__code__.co_flags & inspect.CO_ITERABLE_COROUTINE)
    CoroutineTests.assertFalse(gen.__code__.co_flags & inspect.CO_COROUTINE)
    g = gen()
    CoroutineTests.assertTrue(g.gi_code.co_flags & inspect.CO_ITERABLE_COROUTINE)
    CoroutineTests.assertFalse(g.gi_code.co_flags & inspect.CO_COROUTINE)
    CoroutineTests.assertIs(types.coroutine(gen), gen)

CoroutineTests = test_types.CoroutineTests()
test_genfunc()
