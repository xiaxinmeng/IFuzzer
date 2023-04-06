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

def test_no_order():

    @dataclass(order=False)
    class C:
        x: int
    TestOrdering.assertNotIn('__le__', C.__dict__)
    TestOrdering.assertNotIn('__lt__', C.__dict__)
    TestOrdering.assertNotIn('__ge__', C.__dict__)
    TestOrdering.assertNotIn('__gt__', C.__dict__)

    @dataclass(order=False)
    class C:
        x: int

        def __lt__(TestOrdering, other):
            return False
    TestOrdering.assertNotIn('__le__', C.__dict__)
    TestOrdering.assertNotIn('__ge__', C.__dict__)
    TestOrdering.assertNotIn('__gt__', C.__dict__)

TestOrdering = test_dataclasses.TestOrdering()
test_no_order()
