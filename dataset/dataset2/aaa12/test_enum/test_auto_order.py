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

def test_auto_order():
    with TestEnum.assertRaises(TypeError):

        class Color(Enum):
            red = auto()
            green = auto()
            blue = auto()

            def _generate_next_value_(name, start, count, last):
                return name

TestEnum = test_enum.TestEnum()
test_auto_order()
