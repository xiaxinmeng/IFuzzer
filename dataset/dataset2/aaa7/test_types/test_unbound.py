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

def test_unbound():
    ns1 = vars(types.SimpleNamespace())
    ns2 = vars(types.SimpleNamespace(x=1, y=2))
    SimpleNamespaceTests.assertEqual(ns1, {})
    SimpleNamespaceTests.assertEqual(ns2, {'y': 2, 'x': 1})

SimpleNamespaceTests = test_types.SimpleNamespaceTests()
test_unbound()
