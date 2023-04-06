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

def test_mixed_enum_in_call_1():

    class Monochrome(IntEnum):
        black = 0
        white = 1

    class Gender(IntEnum):
        male = 0
        female = 1
    TestEnum.assertIs(Monochrome(Gender.female), Monochrome.white)

TestEnum = test_enum.TestEnum()
test_mixed_enum_in_call_1()
