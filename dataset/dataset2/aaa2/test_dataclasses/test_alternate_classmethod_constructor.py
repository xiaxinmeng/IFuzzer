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

def test_alternate_classmethod_constructor():

    @dataclass
    class C:
        x: int

        @classmethod
        def from_file(cls, filename):
            value_in_file = 20
            return cls(value_in_file)
    TestCase.assertEqual(C.from_file('filename').x, 20)

TestCase = test_dataclasses.TestCase()
test_alternate_classmethod_constructor()
