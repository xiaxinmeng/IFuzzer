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

def test_overwriting_init():

    @dataclass
    class C:
        x: int

        def __init__(TestInit, x):
            TestInit.x = 2 * x
    TestInit.assertEqual(C(3).x, 6)

    @dataclass(init=True)
    class C:
        x: int

        def __init__(TestInit, x):
            TestInit.x = 2 * x
    TestInit.assertEqual(C(4).x, 8)

    @dataclass(init=False)
    class C:
        x: int

        def __init__(TestInit, x):
            TestInit.x = 2 * x
    TestInit.assertEqual(C(5).x, 10)

TestInit = test_dataclasses.TestInit()
test_overwriting_init()
