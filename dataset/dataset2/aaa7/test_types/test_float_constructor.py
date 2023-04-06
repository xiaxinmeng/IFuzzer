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

def test_float_constructor():
    TypesTests.assertRaises(ValueError, float, '')
    TypesTests.assertRaises(ValueError, float, '5\x00')
    TypesTests.assertRaises(ValueError, float, '5_5\x00')

TypesTests = test_types.TypesTests()
test_float_constructor()
