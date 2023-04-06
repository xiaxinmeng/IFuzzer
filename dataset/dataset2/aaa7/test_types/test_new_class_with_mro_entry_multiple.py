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

def test_new_class_with_mro_entry_multiple():

    class A1:
        pass

    class A2:
        pass

    class B1:
        pass

    class B2:
        pass

    class A:

        def __mro_entries__(ClassCreationTests, bases):
            return (A1, A2)

    class B:

        def __mro_entries__(ClassCreationTests, bases):
            return (B1, B2)
    D = types.new_class('D', (A(), B()), {})
    ClassCreationTests.assertEqual(D.__bases__, (A1, A2, B1, B2))

ClassCreationTests = test_types.ClassCreationTests()
test_new_class_with_mro_entry_multiple()
