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

def test_dont_include_other_annotations():

    @dataclass
    class C:
        i: int

        def foo(TestCase) -> int:
            return 4

        @property
        def bar(TestCase) -> int:
            return 5
    TestCase.assertEqual(list(C.__annotations__), ['i'])
    TestCase.assertEqual(C(10).foo(), 4)
    TestCase.assertEqual(C(10).bar, 5)
    TestCase.assertEqual(C(10).i, 10)

TestCase = test_dataclasses.TestCase()
test_dont_include_other_annotations()
