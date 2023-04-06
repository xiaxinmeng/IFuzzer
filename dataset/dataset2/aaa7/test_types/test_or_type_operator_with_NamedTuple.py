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

def test_or_type_operator_with_NamedTuple():
    NT = namedtuple('A', ['B', 'C', 'D'])
    assert NT | str == typing.Union[NT, str]

TypesTests = test_types.TypesTests()
test_or_type_operator_with_NamedTuple()
