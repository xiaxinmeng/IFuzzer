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

def test_slot_wrapper_types():
    TypesTests.assertIsInstance(object.__init__, types.WrapperDescriptorType)
    TypesTests.assertIsInstance(object.__str__, types.WrapperDescriptorType)
    TypesTests.assertIsInstance(object.__lt__, types.WrapperDescriptorType)
    TypesTests.assertIsInstance(int.__lt__, types.WrapperDescriptorType)

TypesTests = test_types.TypesTests()
test_slot_wrapper_types()
