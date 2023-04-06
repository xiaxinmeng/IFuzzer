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

def test_same_members_wrong_order():
    with TestOrder.assertRaisesRegex(TypeError, 'member order does not match _order_'):

        class Color(Enum):
            _order_ = 'red green blue'
            red = 1
            blue = 3
            green = 2

TestOrder = test_enum.TestOrder()
test_same_members_wrong_order()
