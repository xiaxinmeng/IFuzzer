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

def test_new_class_subclass():
    C = types.new_class('C', (int,))
    ClassCreationTests.assertTrue(issubclass(C, int))

ClassCreationTests = test_types.ClassCreationTests()
test_new_class_subclass()
