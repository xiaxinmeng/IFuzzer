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

def test_zero_division():
    try:
        5.0 / 0.0
    except ZeroDivisionError:
        pass
    else:
        TypesTests.fail("5.0 / 0.0 didn't raise ZeroDivisionError")
    try:
        5.0 // 0.0
    except ZeroDivisionError:
        pass
    else:
        TypesTests.fail("5.0 // 0.0 didn't raise ZeroDivisionError")
    try:
        5.0 % 0.0
    except ZeroDivisionError:
        pass
    else:
        TypesTests.fail("5.0 % 0.0 didn't raise ZeroDivisionError")
    try:
        5 / 0
    except ZeroDivisionError:
        pass
    else:
        TypesTests.fail("5 / 0 didn't raise ZeroDivisionError")
    try:
        5 // 0
    except ZeroDivisionError:
        pass
    else:
        TypesTests.fail("5 // 0 didn't raise ZeroDivisionError")
    try:
        5 % 0
    except ZeroDivisionError:
        pass
    else:
        TypesTests.fail("5 % 0 didn't raise ZeroDivisionError")

TypesTests = test_types.TypesTests()
test_zero_division()
