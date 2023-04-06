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

def test_notimplemented_type():
    TypesTests.assertIsInstance(NotImplemented, types.NotImplementedType)

TypesTests = test_types.TypesTests()
test_notimplemented_type()
