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

def test_internal_sizes():
    TypesTests.assertGreater(object.__basicsize__, 0)
    TypesTests.assertGreater(tuple.__itemsize__, 0)

TypesTests = test_types.TypesTests()
test_internal_sizes()
