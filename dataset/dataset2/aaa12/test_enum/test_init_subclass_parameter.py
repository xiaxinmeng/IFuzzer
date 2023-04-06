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

def test_init_subclass_parameter():

    class multiEnum(Enum):

        def __init_subclass__(cls, multi):
            for member in cls:
                member._as_parameter_ = multi * member.value

    class E(multiEnum, multi=3):
        A = 1
        B = 2
    TestEnum.assertEqual(E.A._as_parameter_, 3)
    TestEnum.assertEqual(E.B._as_parameter_, 6)

TestEnum = test_enum.TestEnum()
test_init_subclass_parameter()
