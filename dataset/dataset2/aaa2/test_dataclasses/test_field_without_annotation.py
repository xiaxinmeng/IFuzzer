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

def test_field_without_annotation():
    with TestFieldNoAnnotation.assertRaisesRegex(TypeError, "'f' is a field but has no type annotation"):

        @dataclass
        class C:
            f = field()

TestFieldNoAnnotation = test_dataclasses.TestFieldNoAnnotation()
test_field_without_annotation()
