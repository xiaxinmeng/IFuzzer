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

def test_missing():

    class dictmissing(dict):

        def __missing__(MappingProxyTests, key):
            return 'missing=%s' % key
    view = MappingProxyTests.mappingproxy(dictmissing(x=1))
    MappingProxyTests.assertEqual(view['x'], 1)
    MappingProxyTests.assertEqual(view['y'], 'missing=y')
    MappingProxyTests.assertEqual(view.get('x'), 1)
    MappingProxyTests.assertEqual(view.get('y'), None)
    MappingProxyTests.assertEqual(view.get('y', 42), 42)
    MappingProxyTests.assertTrue('x' in view)
    MappingProxyTests.assertFalse('y' in view)

MappingProxyTests = test_types.MappingProxyTests()
test_missing()
