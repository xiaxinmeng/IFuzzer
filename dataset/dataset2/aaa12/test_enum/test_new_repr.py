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

def test_new_repr():

    class Color(Enum):
        red = 1
        green = 2
        blue = 3

        def __repr__(TestEnum):
            return "don't you just love shades of %s?" % TestEnum.name
    TestEnum.assertEqual(repr(Color.blue), "don't you just love shades of blue?")

TestEnum = test_enum.TestEnum()
test_new_repr()
