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

def test_methods():
    attrs = set(dir(MappingProxyTests.mappingproxy({}))) - set(dir(object()))
    MappingProxyTests.assertEqual(attrs, {'__contains__', '__getitem__', '__class_getitem__', '__ior__', '__iter__', '__len__', '__or__', '__reversed__', '__ror__', 'copy', 'get', 'items', 'keys', 'values'})

MappingProxyTests = test_types.MappingProxyTests()
test_methods()
