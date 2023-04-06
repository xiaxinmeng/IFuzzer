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

def test_underlying_dict():
    ns1 = types.SimpleNamespace()
    ns2 = types.SimpleNamespace(x=1, y=2)
    ns3 = types.SimpleNamespace(a=True, b=False)
    mapping = ns3.__dict__
    del ns3
    SimpleNamespaceTests.assertEqual(ns1.__dict__, {})
    SimpleNamespaceTests.assertEqual(ns2.__dict__, {'y': 2, 'x': 1})
    SimpleNamespaceTests.assertEqual(mapping, dict(a=True, b=False))

SimpleNamespaceTests = test_types.SimpleNamespaceTests()
test_underlying_dict()
