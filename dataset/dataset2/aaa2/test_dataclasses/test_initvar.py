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

def test_initvar():
    for typestr in ('InitVar[int]', 'InitVar [int] InitVar [int]', 'InitVar', ' InitVar ', 'dataclasses.InitVar[int]', 'dataclasses.InitVar[str]', ' dataclasses.InitVar[str]', 'dataclasses .InitVar[str]', 'dataclasses. InitVar[str]', 'dataclasses.InitVar [str]', 'dataclasses.InitVar [ str]', '"dataclasses.InitVar[int]"', 'dataclasses.InitVar.[int]', 'dataclasses.InitVar+'):
        with TestStringAnnotations.subTest(typestr=typestr):
            C = dataclass(type('C', (), {'__annotations__': {'x': typestr}}))
            with TestStringAnnotations.assertRaisesRegex(AttributeError, "object has no attribute 'x'"):
                C(1).x

TestStringAnnotations = test_dataclasses.TestStringAnnotations()
test_initvar()
