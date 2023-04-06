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

def test_subclass():

    class Spam(types.SimpleNamespace):
        pass
    spam = Spam(ham=8, eggs=9)
    SimpleNamespaceTests.assertIs(type(spam), Spam)
    SimpleNamespaceTests.assertEqual(vars(spam), {'ham': 8, 'eggs': 9})

SimpleNamespaceTests = test_types.SimpleNamespaceTests()
test_subclass()
