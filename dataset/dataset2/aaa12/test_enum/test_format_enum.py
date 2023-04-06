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

def test_format_enum():
    Season = TestEnum.Season
    TestEnum.assertEqual('{}'.format(Season.SPRING), '{}'.format(str(Season.SPRING)))
    TestEnum.assertEqual('{:}'.format(Season.SPRING), '{:}'.format(str(Season.SPRING)))
    TestEnum.assertEqual('{:20}'.format(Season.SPRING), '{:20}'.format(str(Season.SPRING)))
    TestEnum.assertEqual('{:^20}'.format(Season.SPRING), '{:^20}'.format(str(Season.SPRING)))
    TestEnum.assertEqual('{:>20}'.format(Season.SPRING), '{:>20}'.format(str(Season.SPRING)))
    TestEnum.assertEqual('{:<20}'.format(Season.SPRING), '{:<20}'.format(str(Season.SPRING)))

TestEnum = test_enum.TestEnum()
TestEnum.setUp()
test_format_enum()
