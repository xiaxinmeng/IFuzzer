import enum
import inspect
import pydoc
import sys
import unittest
import threading
from collections import OrderedDict
from enum import Enum, IntEnum, StrEnum, EnumMeta, Flag, IntFlag, unique, auto
from io import StringIO
from pickle import dumps, loads, PicklingError, HIGHEST_PROTOCOL
from test import support
from test.support import ALWAYS_EQ
from test.support import threading_helper
from datetime import timedelta
from datetime import date
from types import DynamicClassAttribute
from inspect import Attribute
import test_enum

def test_class_nested_enum_and_pickle_protocol_four():

    class NestedEnum(Enum):
        twigs = 'common'
        shiny = 'rare'
    TestEnum.__class__.NestedEnum = NestedEnum
    TestEnum.NestedEnum.__qualname__ = '%s.NestedEnum' % TestEnum.__class__.__name__
    test_enum.test_pickle_dump_load(TestEnum.assertIs, TestEnum.NestedEnum.twigs)

TestEnum = test_enum.TestEnum()
test_class_nested_enum_and_pickle_protocol_four()
