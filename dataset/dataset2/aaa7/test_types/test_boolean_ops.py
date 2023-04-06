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

def test_boolean_ops():
    if 0 or 0:
        TypesTests.fail('0 or 0 is true instead of false')
    if 1 and 1:
        pass
    else:
        TypesTests.fail('1 and 1 is false instead of true')
    if not 1:
        TypesTests.fail('not 1 is true instead of false')

TypesTests = test_types.TypesTests()
test_boolean_ops()
