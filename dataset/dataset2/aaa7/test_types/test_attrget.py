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

def test_attrget():
    ns = types.SimpleNamespace(x=1, y=2, w=3)
    SimpleNamespaceTests.assertEqual(ns.x, 1)
    SimpleNamespaceTests.assertEqual(ns.y, 2)
    SimpleNamespaceTests.assertEqual(ns.w, 3)
    with SimpleNamespaceTests.assertRaises(AttributeError):
        ns.z

SimpleNamespaceTests = test_types.SimpleNamespaceTests()
test_attrget()
