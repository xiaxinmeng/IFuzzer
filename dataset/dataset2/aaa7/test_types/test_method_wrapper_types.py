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

def test_method_wrapper_types():
    TypesTests.assertIsInstance(object().__init__, types.MethodWrapperType)
    TypesTests.assertIsInstance(object().__str__, types.MethodWrapperType)
    TypesTests.assertIsInstance(object().__lt__, types.MethodWrapperType)
    TypesTests.assertIsInstance(42 .__lt__, types.MethodWrapperType)

TypesTests = test_types.TypesTests()
test_method_wrapper_types()
