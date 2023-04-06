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

def test_or_type_operator_with_TypeVar():
    TV = typing.TypeVar('T')
    assert TV | str == typing.Union[TV, str]
    assert str | TV == typing.Union[str, TV]

TypesTests = test_types.TypesTests()
test_or_type_operator_with_TypeVar()
