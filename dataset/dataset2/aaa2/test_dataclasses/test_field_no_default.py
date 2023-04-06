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

def test_field_no_default():

    @dataclass
    class C:
        x: int = field()
    TestCase.assertEqual(C(5).x, 5)
    with TestCase.assertRaisesRegex(TypeError, "__init__\\(\\) missing 1 required positional argument: 'x'"):
        C()

TestCase = test_dataclasses.TestCase()
test_field_no_default()
