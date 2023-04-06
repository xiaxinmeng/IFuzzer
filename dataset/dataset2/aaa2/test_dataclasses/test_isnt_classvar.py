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

def test_isnt_classvar():
    for typestr in ('CV', 't.ClassVar', 't.ClassVar[int]', 'typing..ClassVar[int]', 'Classvar', 'Classvar[int]', 'typing.ClassVarx[int]', 'typong.ClassVar[int]', 'dataclasses.ClassVar[int]', 'typingxClassVar[str]'):
        with TestStringAnnotations.subTest(typestr=typestr):
            C = dataclass(type('C', (), {'__annotations__': {'x': typestr}}))
            TestStringAnnotations.assertEqual(C(10).x, 10)

TestStringAnnotations = test_dataclasses.TestStringAnnotations()
test_isnt_classvar()
