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

def test_pickle_by_name():

    class ReplaceGlobalInt(IntEnum):
        ONE = 1
        TWO = 2
    ReplaceGlobalInt.__reduce_ex__ = enum._reduce_ex_by_name
    for proto in range(HIGHEST_PROTOCOL):
        TestEnum.assertEqual(ReplaceGlobalInt.TWO.__reduce_ex__(proto), 'TWO')

TestEnum = test_enum.TestEnum()
test_pickle_by_name()
