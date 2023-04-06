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

def test_or_type_repr():
    assert repr(int | None) == 'int | None'
    assert repr(int | typing.GenericAlias(list, int)) == 'int | list[int]'

TypesTests = test_types.TypesTests()
test_or_type_repr()
