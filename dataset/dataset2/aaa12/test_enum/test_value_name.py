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

def test_value_name():
    Season = TestEnum.Season
    TestEnum.assertEqual(Season.SPRING.name, 'SPRING')
    TestEnum.assertEqual(Season.SPRING.value, 1)
    with TestEnum.assertRaises(AttributeError):
        Season.SPRING.name = 'invierno'
    with TestEnum.assertRaises(AttributeError):
        Season.SPRING.value = 2

TestEnum = test_enum.TestEnum()
TestEnum.setUp()
test_value_name()
