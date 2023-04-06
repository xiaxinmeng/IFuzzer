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

def test_hash():
    Season = TestEnum.Season
    dates = {}
    dates[Season.WINTER] = '1225'
    dates[Season.SPRING] = '0315'
    dates[Season.SUMMER] = '0704'
    dates[Season.AUTUMN] = '1031'
    TestEnum.assertEqual(dates[Season.AUTUMN], '1031')

TestEnum = test_enum.TestEnum()
TestEnum.setUp()
test_hash()
