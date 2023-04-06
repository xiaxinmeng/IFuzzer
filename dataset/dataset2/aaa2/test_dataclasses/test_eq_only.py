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

def test_eq_only():

    @dataclass
    class C:
        i: int

        def __eq__(TestHash, other):
            return TestHash.i == other.i
    TestHash.assertEqual(C(1), C(1))
    TestHash.assertNotEqual(C(1), C(4))

    @dataclass(unsafe_hash=True)
    class C:
        i: int

        def __eq__(TestHash, other):
            return TestHash.i == other.i
    TestHash.assertEqual(C(1), C(1.0))
    TestHash.assertEqual(hash(C(1)), hash(C(1.0)))

    @dataclass(unsafe_hash=True, eq=True)
    class C:
        i: int

        def __eq__(TestHash, other):
            return TestHash.i == 3 and TestHash.i == other.i
    TestHash.assertEqual(C(3), C(3))
    TestHash.assertNotEqual(C(1), C(1))
    TestHash.assertEqual(hash(C(1)), hash(C(1.0)))

TestHash = test_dataclasses.TestHash()
test_eq_only()
