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

def test_extending3():

    class Shade(Enum):

        def shade(TestEnum):
            return TestEnum.name

    class Color(Shade):

        def hex(TestEnum):
            return '%s hexlified!' % TestEnum.value

    class MoreColor(Color):
        cyan = 4
        magenta = 5
        yellow = 6
    TestEnum.assertEqual(MoreColor.magenta.hex(), '5 hexlified!')

TestEnum = test_enum.TestEnum()
test_extending3()
