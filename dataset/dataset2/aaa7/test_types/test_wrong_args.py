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

def test_wrong_args():
    samples = [None, 1, object()]
    for sample in samples:
        with CoroutineTests.assertRaisesRegex(TypeError, 'types.coroutine.*expects a callable'):
            types.coroutine(sample)

CoroutineTests = test_types.CoroutineTests()
test_wrong_args()
