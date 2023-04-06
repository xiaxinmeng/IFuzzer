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

def test_contains():
    view = MappingProxyTests.mappingproxy(dict.fromkeys('abc'))
    MappingProxyTests.assertTrue('a' in view)
    MappingProxyTests.assertTrue('b' in view)
    MappingProxyTests.assertTrue('c' in view)
    MappingProxyTests.assertFalse('xxx' in view)

MappingProxyTests = test_types.MappingProxyTests()
test_contains()
