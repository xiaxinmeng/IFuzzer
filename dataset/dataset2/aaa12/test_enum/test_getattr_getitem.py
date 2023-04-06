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

def test_getattr_getitem():

    class Period(Enum):
        morning = 1
        noon = 2
        evening = 3
        night = 4
    TestEnum.assertIs(Period(2), Period.noon)
    TestEnum.assertIs(getattr(Period, 'night'), Period.night)
    TestEnum.assertIs(Period['morning'], Period.morning)

TestEnum = test_enum.TestEnum()
TestEnum.setUp()
test_getattr_getitem()
