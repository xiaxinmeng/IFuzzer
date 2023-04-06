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

def test_conflicting_types_resolved_in_new():

    class LabelledIntEnum(int, Enum):

        def __new__(cls, *args):
            (value, label) = args
            obj = int.__new__(cls, value)
            obj.label = label
            obj._value_ = value
            return obj

    class LabelledList(LabelledIntEnum):
        unprocessed = (1, 'Unprocessed')
        payment_complete = (2, 'Payment Complete')
    TestEnum.assertEqual(list(LabelledList), [LabelledList.unprocessed, LabelledList.payment_complete])
    TestEnum.assertEqual(LabelledList.unprocessed, 1)
    TestEnum.assertEqual(LabelledList(1), LabelledList.unprocessed)

TestEnum = test_enum.TestEnum()
test_conflicting_types_resolved_in_new()
