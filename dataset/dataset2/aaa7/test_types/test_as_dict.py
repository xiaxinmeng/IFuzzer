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

def test_as_dict():
    ns = types.SimpleNamespace(spam='spamspamspam')
    with SimpleNamespaceTests.assertRaises(TypeError):
        len(ns)
    with SimpleNamespaceTests.assertRaises(TypeError):
        iter(ns)
    with SimpleNamespaceTests.assertRaises(TypeError):
        'spam' in ns
    with SimpleNamespaceTests.assertRaises(TypeError):
        ns['spam']

SimpleNamespaceTests = test_types.SimpleNamespaceTests()
test_as_dict()
