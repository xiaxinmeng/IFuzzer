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

def test_new_class_basics():
    C = types.new_class('C')
    ClassCreationTests.assertEqual(C.__name__, 'C')
    ClassCreationTests.assertEqual(C.__bases__, (object,))

ClassCreationTests = test_types.ClassCreationTests()
test_new_class_basics()
