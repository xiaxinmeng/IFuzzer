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

def test_fake_namespace_compare():

    class FakeSimpleNamespace(str):
        __class__ = types.SimpleNamespace
    SimpleNamespaceTests.assertFalse(types.SimpleNamespace() == FakeSimpleNamespace())
    SimpleNamespaceTests.assertTrue(types.SimpleNamespace() != FakeSimpleNamespace())
    with SimpleNamespaceTests.assertRaises(TypeError):
        types.SimpleNamespace() < FakeSimpleNamespace()
    with SimpleNamespaceTests.assertRaises(TypeError):
        types.SimpleNamespace() <= FakeSimpleNamespace()
    with SimpleNamespaceTests.assertRaises(TypeError):
        types.SimpleNamespace() > FakeSimpleNamespace()
    with SimpleNamespaceTests.assertRaises(TypeError):
        types.SimpleNamespace() >= FakeSimpleNamespace()

SimpleNamespaceTests = test_types.SimpleNamespaceTests()
test_fake_namespace_compare()
