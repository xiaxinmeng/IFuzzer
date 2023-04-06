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

def test_overwriting_eq():

    @dataclass
    class C:
        x: int

        def __eq__(TestEq, other):
            return other == 3
    TestEq.assertEqual(C(1), 3)
    TestEq.assertNotEqual(C(1), 1)

    @dataclass(eq=True)
    class C:
        x: int

        def __eq__(TestEq, other):
            return other == 4
    TestEq.assertEqual(C(1), 4)
    TestEq.assertNotEqual(C(1), 1)

    @dataclass(eq=False)
    class C:
        x: int

        def __eq__(TestEq, other):
            return other == 5
    TestEq.assertEqual(C(1), 5)
    TestEq.assertNotEqual(C(1), 1)

TestEq = test_dataclasses.TestEq()
test_overwriting_eq()
