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

def test_no_types():
    C = make_dataclass('Point', ['x', 'y', 'z'])
    c = C(1, 2, 3)
    TestMakeDataclass.assertEqual(vars(c), {'x': 1, 'y': 2, 'z': 3})
    TestMakeDataclass.assertEqual(C.__annotations__, {'x': 'typing.Any', 'y': 'typing.Any', 'z': 'typing.Any'})
    C = make_dataclass('Point', ['x', ('y', int), 'z'])
    c = C(1, 2, 3)
    TestMakeDataclass.assertEqual(vars(c), {'x': 1, 'y': 2, 'z': 3})
    TestMakeDataclass.assertEqual(C.__annotations__, {'x': 'typing.Any', 'y': int, 'z': 'typing.Any'})

TestMakeDataclass = test_dataclasses.TestMakeDataclass()
test_no_types()
