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

def test_helper_asdict_builtin_object_containers():

    @dataclass
    class Child:
        d: object

    @dataclass
    class Parent:
        child: Child
    TestCase.assertEqual(asdict(Parent(Child([1]))), {'child': {'d': [1]}})
    TestCase.assertEqual(asdict(Parent(Child({1: 2}))), {'child': {'d': {1: 2}}})

TestCase = test_dataclasses.TestCase()
test_helper_asdict_builtin_object_containers()
