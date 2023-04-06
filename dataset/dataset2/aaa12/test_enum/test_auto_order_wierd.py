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

def test_auto_order_wierd():
    weird_auto = auto()
    weird_auto.value = 'pathological case'

    class Color(Enum):
        red = weird_auto

        def _generate_next_value_(name, start, count, last):
            return name
        blue = auto()
    TestEnum.assertEqual(list(Color), [Color.red, Color.blue])
    TestEnum.assertEqual(Color.red.value, 'pathological case')
    TestEnum.assertEqual(Color.blue.value, 'blue')

TestEnum = test_enum.TestEnum()
test_auto_order_wierd()
