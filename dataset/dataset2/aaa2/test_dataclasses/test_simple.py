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

def test_simple():
    C = make_dataclass('C', [('x', int), ('y', int, field(default=5))], namespace={'add_one': lambda TestSlots: TestSlots.x + 1})
    c = C(10)
    TestSlots.assertEqual((c.x, c.y), (10, 5))
    TestSlots.assertEqual(c.add_one(), 11)

TestSlots = test_dataclasses.TestSlots()
test_simple()
