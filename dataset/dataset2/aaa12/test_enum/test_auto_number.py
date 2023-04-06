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

def test_auto_number():

    class Color(Flag):
        red = auto()
        blue = auto()
        green = auto()
    TestEnum.assertEqual(list(Color), [Color.red, Color.blue, Color.green])
    TestEnum.assertEqual(Color.red.value, 1)
    TestEnum.assertEqual(Color.blue.value, 2)
    TestEnum.assertEqual(Color.green.value, 4)

TestEnum = test_enum.TestEnum()
test_auto_number()
