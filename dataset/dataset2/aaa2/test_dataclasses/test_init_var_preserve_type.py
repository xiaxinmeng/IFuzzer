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

def test_init_var_preserve_type():
    TestCase.assertEqual(InitVar[int].type, int)
    TestCase.assertEqual(repr(InitVar[int]), 'dataclasses.InitVar[int]')
    TestCase.assertEqual(repr(InitVar[List[int]]), 'dataclasses.InitVar[typing.List[int]]')

TestCase = test_dataclasses.TestCase()
test_init_var_preserve_type()
