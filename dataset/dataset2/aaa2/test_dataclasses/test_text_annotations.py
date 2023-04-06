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

def test_text_annotations():
    from test import dataclass_textanno
    TestStringAnnotations.assertEqual(get_type_hints(dataclass_textanno.Bar), {'foo': dataclass_textanno.Foo})
    TestStringAnnotations.assertEqual(get_type_hints(dataclass_textanno.Bar.__init__), {'foo': dataclass_textanno.Foo, 'return': type(None)})

TestStringAnnotations = test_dataclasses.TestStringAnnotations()
test_text_annotations()
