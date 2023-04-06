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

def test_floats():
    if 12.0 + 24.0 != 36.0:
        TypesTests.fail('float op')
    if 12.0 + -24.0 != -12.0:
        TypesTests.fail('float op')
    if -12.0 + 24.0 != 12.0:
        TypesTests.fail('float op')
    if -12.0 + -24.0 != -36.0:
        TypesTests.fail('float op')
    if not 12.0 < 24.0:
        TypesTests.fail('float op')
    if not -24.0 < -12.0:
        TypesTests.fail('float op')

TypesTests = test_types.TypesTests()
test_floats()
