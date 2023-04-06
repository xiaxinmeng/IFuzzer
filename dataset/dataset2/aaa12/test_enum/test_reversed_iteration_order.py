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

def test_reversed_iteration_order():
    TestEnum.assertEqual(list(reversed(TestEnum.Season)), [TestEnum.Season.WINTER, TestEnum.Season.AUTUMN, TestEnum.Season.SUMMER, TestEnum.Season.SPRING])

TestEnum = test_enum.TestEnum()
TestEnum.setUp()
test_reversed_iteration_order()
