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

def test_post_init_super():

    class B:

        def __post_init__(TestCase):
            raise test_dataclasses.CustomError()

    @dataclass
    class C(B):

        def __post_init__(TestCase):
            TestCase.x = 5
    TestCase.assertEqual(C().x, 5)

    @dataclass
    class C(B):

        def __post_init__(TestCase):
            super().__post_init__()
    with TestCase.assertRaises(test_dataclasses.CustomError):
        C()

    @dataclass
    class C(B):
        pass
    with TestCase.assertRaises(test_dataclasses.CustomError):
        C()

TestCase = test_dataclasses.TestCase()
test_post_init_super()
