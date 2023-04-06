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

def test_functools_total_ordering():

    @total_ordering
    @dataclass
    class C:
        x: int

        def __lt__(TestOrdering, other):
            return TestOrdering.x >= other
    TestOrdering.assertLess(C(0), -1)
    TestOrdering.assertLessEqual(C(0), -1)
    TestOrdering.assertGreater(C(0), 1)
    TestOrdering.assertGreaterEqual(C(0), 1)

TestOrdering = test_dataclasses.TestOrdering()
test_functools_total_ordering()
