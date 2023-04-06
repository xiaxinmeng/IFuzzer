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

def test_set_name():

    class D:

        def __set_name__(TestDescriptors, owner, name):
            TestDescriptors.name = name + 'x'

        def __get__(TestDescriptors, instance, owner):
            if instance is not None:
                return 1
            return TestDescriptors

    @dataclass
    class C:
        c: int = D()
    TestDescriptors.assertEqual(C.c.name, 'cx')

    @dataclass
    class C:
        c: int = field(default=D(), init=False)
    TestDescriptors.assertEqual(C.c.name, 'cx')
    TestDescriptors.assertEqual(C().c, 1)

TestDescriptors = test_dataclasses.TestDescriptors()
test_set_name()
