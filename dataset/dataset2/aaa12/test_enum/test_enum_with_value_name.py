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

def test_enum_with_value_name():

    class Huh(Enum):
        name = 1
        value = 2
    TestEnum.assertEqual(list(Huh), [Huh.name, Huh.value])
    TestEnum.assertIs(type(Huh.name), Huh)
    TestEnum.assertEqual(Huh.name.name, 'name')
    TestEnum.assertEqual(Huh.name.value, 1)

TestEnum = test_enum.TestEnum()
test_enum_with_value_name()
