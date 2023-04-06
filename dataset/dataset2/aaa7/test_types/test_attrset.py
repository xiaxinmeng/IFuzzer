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

def test_attrset():
    ns1 = types.SimpleNamespace()
    ns2 = types.SimpleNamespace(x=1, y=2, w=3)
    ns1.a = 'spam'
    ns1.b = 'ham'
    ns2.z = 4
    ns2.theta = None
    SimpleNamespaceTests.assertEqual(ns1.__dict__, dict(a='spam', b='ham'))
    SimpleNamespaceTests.assertEqual(ns2.__dict__, dict(x=1, y=2, w=3, z=4, theta=None))

SimpleNamespaceTests = test_types.SimpleNamespaceTests()
test_attrset()
