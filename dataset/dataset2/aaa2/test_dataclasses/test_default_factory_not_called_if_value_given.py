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

def test_default_factory_not_called_if_value_given():
    factory = Mock()

    @dataclass
    class C:
        x: int = field(default_factory=factory)
    C().x
    TestCase.assertEqual(factory.call_count, 1)
    TestCase.assertEqual(C(10).x, 10)
    TestCase.assertEqual(factory.call_count, 1)
    C().x
    TestCase.assertEqual(factory.call_count, 2)

TestCase = test_dataclasses.TestCase()
test_default_factory_not_called_if_value_given()
