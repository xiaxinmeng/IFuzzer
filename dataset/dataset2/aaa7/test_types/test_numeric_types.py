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

def test_numeric_types():
    if 0 != 0.0 or 1 != 1.0 or -1 != -1.0:
        TypesTests.fail('int/float value not equal')
    if int() != 0:
        TypesTests.fail('int() does not return 0')
    if float() != 0.0:
        TypesTests.fail('float() does not return 0.0')
    if int(1.9) == 1 == int(1.1) and int(-1.1) == -1 == int(-1.9):
        pass
    else:
        TypesTests.fail('int() does not round properly')
    if float(1) == 1.0 and float(-1) == -1.0 and (float(0) == 0.0):
        pass
    else:
        TypesTests.fail('float() does not work properly')

TypesTests = test_types.TypesTests()
test_numeric_types()
