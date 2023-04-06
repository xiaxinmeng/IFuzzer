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

def test_format_enum_float():
    Konstants = TestEnum.Konstants
    TestEnum.assertFormatIsValue('{}', Konstants.TAU)
    TestEnum.assertFormatIsValue('{:}', Konstants.TAU)
    TestEnum.assertFormatIsValue('{:20}', Konstants.TAU)
    TestEnum.assertFormatIsValue('{:^20}', Konstants.TAU)
    TestEnum.assertFormatIsValue('{:>20}', Konstants.TAU)
    TestEnum.assertFormatIsValue('{:<20}', Konstants.TAU)
    TestEnum.assertFormatIsValue('{:n}', Konstants.TAU)
    TestEnum.assertFormatIsValue('{:5.2}', Konstants.TAU)
    TestEnum.assertFormatIsValue('{:f}', Konstants.TAU)

TestEnum = test_enum.TestEnum()
TestEnum.setUp()
test_format_enum_float()
