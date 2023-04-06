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

def test_repr():
    ns1 = types.SimpleNamespace(x=1, y=2, w=3)
    ns2 = types.SimpleNamespace()
    ns2.x = 'spam'
    ns2._y = 5
    name = 'namespace'
    SimpleNamespaceTests.assertEqual(repr(ns1), '{name}(x=1, y=2, w=3)'.format(name=name))
    SimpleNamespaceTests.assertEqual(repr(ns2), "{name}(x='spam', _y=5)".format(name=name))

SimpleNamespaceTests = test_types.SimpleNamespaceTests()
test_repr()
