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

def test_unsafe_hash():

    @dataclass(unsafe_hash=True)
    class C:
        x: int
        y: str
    TestHash.assertEqual(hash(C(1, 'foo')), hash((1, 'foo')))

TestHash = test_dataclasses.TestHash()
test_unsafe_hash()
