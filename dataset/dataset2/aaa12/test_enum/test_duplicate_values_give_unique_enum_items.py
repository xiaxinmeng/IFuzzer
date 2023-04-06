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

def test_duplicate_values_give_unique_enum_items():

    class AutoNumber(Enum):
        first = ()
        second = ()
        third = ()

        def __new__(cls):
            value = len(cls.__members__) + 1
            obj = object.__new__(cls)
            obj._value_ = value
            return obj

        def __int__(TestEnum):
            return int(TestEnum._value_)
    TestEnum.assertEqual(list(AutoNumber), [AutoNumber.first, AutoNumber.second, AutoNumber.third])
    TestEnum.assertEqual(int(AutoNumber.second), 2)
    TestEnum.assertEqual(AutoNumber.third.value, 3)
    TestEnum.assertIs(AutoNumber(1), AutoNumber.first)

TestEnum = test_enum.TestEnum()
test_duplicate_values_give_unique_enum_items()
