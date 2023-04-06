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

def test_is_dunder():
    for s in ('__a__', '__aa__'):
        TestHelpers.assertTrue(enum._is_dunder(s))
    for s in ('a', 'a_', '_a', '__a', 'a__', '_a_', '_a__', '__a_', '_', '__', '___', '____', '_____'):
        TestHelpers.assertFalse(enum._is_dunder(s))

TestHelpers = test_enum.TestHelpers()
test_is_dunder()
