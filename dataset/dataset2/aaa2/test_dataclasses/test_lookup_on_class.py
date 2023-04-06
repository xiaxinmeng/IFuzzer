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

def test_lookup_on_class():

    class D:
        pass
    D.__set_name__ = Mock()

    @dataclass
    class C:
        i: int = field(default=D(), init=False)
    TestDescriptors.assertEqual(D.__set_name__.call_count, 1)

TestDescriptors = test_dataclasses.TestDescriptors()
test_lookup_on_class()
