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

def test_field_repr():
    int_field = field(default=1, init=True, repr=False)
    int_field.name = 'id'
    repr_output = repr(int_field)
    expected_output = f"Field(name='id',type=None,default=1,default_factory={MISSING!r},init=True,repr=False,hash=None,compare=True,metadata=mappingproxy({{}}),_field_type=None)"
    TestCase.assertEqual(repr_output, expected_output)

TestCase = test_dataclasses.TestCase()
test_field_repr()
