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

def test_not_in_compare():

    @dataclass
    class C:
        x: int = 0
        y: int = field(compare=False, default=4)
    TestCase.assertEqual(C(), C(0, 20))
    TestCase.assertEqual(C(1, 10), C(1, 20))
    TestCase.assertNotEqual(C(3), C(4, 10))
    TestCase.assertNotEqual(C(3, 10), C(4, 10))

TestCase = test_dataclasses.TestCase()
test_not_in_compare()
