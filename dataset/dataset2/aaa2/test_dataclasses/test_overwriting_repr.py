from dataclasses import *
import abc
import pickle
import inspect
import builtins
import unittest
from textwrap import dedent
from unittest.mock import Mock
from typing import ClassVar, Any, List, Union, Tuple, Dict, Generic, TypeVar, Optional
from typing import get_type_hints
from collections import deque, OrderedDict, namedtuple
from functools import total_ordering
import typing
import dataclasses
from test import dataclass_module_1
from test import dataclass_module_2
from test import dataclass_textanno
import test_dataclasses

def test_overwriting_repr():

    @dataclass
    class C:
        x: int

        def __repr__(TestRepr):
            return 'x'
    TestRepr.assertEqual(repr(C(0)), 'x')

    @dataclass(repr=True)
    class C:
        x: int

        def __repr__(TestRepr):
            return 'x'
    TestRepr.assertEqual(repr(C(0)), 'x')

    @dataclass(repr=False)
    class C:
        x: int

        def __repr__(TestRepr):
            return 'x'
    TestRepr.assertEqual(repr(C(0)), 'x')

TestRepr = test_dataclasses.TestRepr()
test_overwriting_repr()
