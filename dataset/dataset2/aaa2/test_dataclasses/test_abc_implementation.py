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

def test_abc_implementation():

    class Ordered(abc.ABC):

        @abc.abstractmethod
        def __lt__(TestAbstract, other):
            pass

        @abc.abstractmethod
        def __le__(TestAbstract, other):
            pass

    @dataclass(order=True)
    class Date(Ordered):
        year: int
        month: 'Month'
        day: 'int'
    TestAbstract.assertFalse(inspect.isabstract(Date))
    TestAbstract.assertGreater(Date(2020, 12, 25), Date(2020, 8, 31))

TestAbstract = test_dataclasses.TestAbstract()
test_abc_implementation()
