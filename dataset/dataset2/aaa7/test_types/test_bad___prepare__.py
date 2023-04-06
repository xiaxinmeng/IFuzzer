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

def test_bad___prepare__():

    class BadMeta(type):

        @classmethod
        def __prepare__(*args):
            return None
    with ClassCreationTests.assertRaisesRegex(TypeError, '^BadMeta\\.__prepare__\\(\\) must return a mapping, not NoneType$'):

        class Foo(metaclass=BadMeta):
            pass

    class BadMeta:

        @classmethod
        def __prepare__(*args):
            return None
    with ClassCreationTests.assertRaisesRegex(TypeError, '^<metaclass>\\.__prepare__\\(\\) must return a mapping, not NoneType$'):

        class Bar(metaclass=BadMeta()):
            pass

ClassCreationTests = test_types.ClassCreationTests()
test_bad___prepare__()
