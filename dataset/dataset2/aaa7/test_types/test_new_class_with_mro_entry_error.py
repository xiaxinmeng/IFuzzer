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

def test_new_class_with_mro_entry_error():

    class A:
        pass

    class C:

        def __mro_entries__(ClassCreationTests, bases):
            return A
    c = C()
    with ClassCreationTests.assertRaises(TypeError):
        types.new_class('D', (c,), {})

ClassCreationTests = test_types.ClassCreationTests()
test_new_class_with_mro_entry_error()
