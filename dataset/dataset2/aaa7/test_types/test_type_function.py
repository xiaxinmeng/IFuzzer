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

def test_type_function():
    TypesTests.assertRaises(TypeError, type, 1, 2)
    TypesTests.assertRaises(TypeError, type, 1, 2, 3, 4)

TypesTests = test_types.TypesTests()
test_type_function()
