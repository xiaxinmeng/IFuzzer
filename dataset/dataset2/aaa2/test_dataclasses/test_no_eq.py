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

def test_no_eq():

    @dataclass(eq=False)
    class C:
        x: int
    TestEq.assertNotEqual(C(0), C(0))
    c = C(3)
    TestEq.assertEqual(c, c)

    @dataclass(eq=False)
    class C:
        x: int

        def __eq__(TestEq, other):
            return other == 10
    TestEq.assertEqual(C(3), 10)

TestEq = test_dataclasses.TestEq()
test_no_eq()
