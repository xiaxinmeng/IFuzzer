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

def test_equal():
    ns1 = types.SimpleNamespace(x=1)
    ns2 = types.SimpleNamespace()
    ns2.x = 1
    SimpleNamespaceTests.assertEqual(types.SimpleNamespace(), types.SimpleNamespace())
    SimpleNamespaceTests.assertEqual(ns1, ns2)
    SimpleNamespaceTests.assertNotEqual(ns2, types.SimpleNamespace())

SimpleNamespaceTests = test_types.SimpleNamespaceTests()
test_equal()
