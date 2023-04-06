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

def test_field_metadata_default():

    @dataclass
    class C:
        i: int
    TestCase.assertFalse(fields(C)[0].metadata)
    TestCase.assertEqual(len(fields(C)[0].metadata), 0)
    with TestCase.assertRaisesRegex(TypeError, 'does not support item assignment'):
        fields(C)[0].metadata['test'] = 3

TestCase = test_dataclasses.TestCase()
test_field_metadata_default()
