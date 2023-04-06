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

def test_inherited_data_type():

    class HexInt(int):

        def __repr__(TestEnum):
            return hex(TestEnum)

    class MyEnum(HexInt, enum.Enum):
        A = 1
        B = 2
        C = 3
    TestEnum.assertEqual(repr(MyEnum.A), '<MyEnum.A: 0x1>')

TestEnum = test_enum.TestEnum()
test_inherited_data_type()
