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

def test_wrapper_object():

    def gen():
        yield

    @types.coroutine
    def coro():
        return gen()
    wrapper = coro()
    CoroutineTests.assertIn('GeneratorWrapper', repr(wrapper))
    CoroutineTests.assertEqual(repr(wrapper), str(wrapper))
    CoroutineTests.assertTrue(set(dir(wrapper)).issuperset({'__await__', '__iter__', '__next__', 'cr_code', 'cr_running', 'cr_frame', 'gi_code', 'gi_frame', 'gi_running', 'send', 'close', 'throw'}))

CoroutineTests = test_types.CoroutineTests()
test_wrapper_object()
