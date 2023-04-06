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

def test_method_descriptor_types():
    TypesTests.assertIsInstance(str.join, types.MethodDescriptorType)
    TypesTests.assertIsInstance(list.append, types.MethodDescriptorType)
    TypesTests.assertIsInstance(''.join, types.BuiltinMethodType)
    TypesTests.assertIsInstance([].append, types.BuiltinMethodType)
    TypesTests.assertIsInstance(int.__dict__['from_bytes'], types.ClassMethodDescriptorType)
    TypesTests.assertIsInstance(int.from_bytes, types.BuiltinMethodType)
    TypesTests.assertIsInstance(int.__new__, types.BuiltinMethodType)

TypesTests = test_types.TypesTests()
test_method_descriptor_types()
