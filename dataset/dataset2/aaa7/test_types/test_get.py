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

def test_get():
    view = MappingProxyTests.mappingproxy({'a': 'A', 'b': 'B'})
    MappingProxyTests.assertEqual(view['a'], 'A')
    MappingProxyTests.assertEqual(view['b'], 'B')
    MappingProxyTests.assertRaises(KeyError, view.__getitem__, 'xxx')
    MappingProxyTests.assertEqual(view.get('a'), 'A')
    MappingProxyTests.assertIsNone(view.get('xxx'))
    MappingProxyTests.assertEqual(view.get('xxx', 42), 42)

MappingProxyTests = test_types.MappingProxyTests()
test_get()
