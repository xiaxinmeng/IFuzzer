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

def test_none_type():
    TypesTests.assertIsInstance(None, types.NoneType)

TypesTests = test_types.TypesTests()
test_none_type()
