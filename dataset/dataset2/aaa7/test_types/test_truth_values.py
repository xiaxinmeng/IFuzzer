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

def test_truth_values():
    if None:
        TypesTests.fail('None is true instead of false')
    if 0:
        TypesTests.fail('0 is true instead of false')
    if 0.0:
        TypesTests.fail('0.0 is true instead of false')
    if '':
        TypesTests.fail("'' is true instead of false")
    if not 1:
        TypesTests.fail('1 is false instead of true')
    if not 1.0:
        TypesTests.fail('1.0 is false instead of true')
    if not 'x':
        TypesTests.fail("'x' is false instead of true")
    if not {'x': 1}:
        TypesTests.fail("{'x': 1} is false instead of true")

    def f():
        pass

    class C:
        pass
    x = C()
    if not f:
        TypesTests.fail('f is false instead of true')
    if not C:
        TypesTests.fail('C is false instead of true')
    if not sys:
        TypesTests.fail('sys is false instead of true')
    if not x:
        TypesTests.fail('x is false instead of true')

TypesTests = test_types.TypesTests()
test_truth_values()
