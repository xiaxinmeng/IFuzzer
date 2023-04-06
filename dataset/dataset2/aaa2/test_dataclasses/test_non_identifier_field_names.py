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

def test_non_identifier_field_names():
    for field in ['()', 'x,y', '*', '2@3', '', 'little johnny tables']:
        with TestMakeDataclass.subTest(field=field):
            with TestMakeDataclass.assertRaisesRegex(TypeError, 'must be valid identifiers'):
                make_dataclass('C', ['a', field])
            with TestMakeDataclass.assertRaisesRegex(TypeError, 'must be valid identifiers'):
                make_dataclass('C', [field])
            with TestMakeDataclass.assertRaisesRegex(TypeError, 'must be valid identifiers'):
                make_dataclass('C', [field, 'a'])

TestMakeDataclass = test_dataclasses.TestMakeDataclass()
test_non_identifier_field_names()
