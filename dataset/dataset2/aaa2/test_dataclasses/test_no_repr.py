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

def test_no_repr():

    @dataclass(repr=False)
    class C:
        x: int
    TestRepr.assertIn(f'{__name__}.TestRepr.test_no_repr.<locals>.C object at', repr(C(3)))

    @dataclass(repr=False)
    class C:
        x: int

        def __repr__(TestRepr):
            return 'C-class'
    TestRepr.assertEqual(repr(C(3)), 'C-class')

TestRepr = test_dataclasses.TestRepr()
test_no_repr()
