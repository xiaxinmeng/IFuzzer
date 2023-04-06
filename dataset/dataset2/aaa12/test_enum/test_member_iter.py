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

def test_member_iter():
    Color = TestIntFlag.Color
    TestIntFlag.assertEqual(list(Color.PURPLE), [Color.BLUE, Color.RED])
    TestIntFlag.assertEqual(list(Color.BLUE), [Color.BLUE])
    TestIntFlag.assertEqual(list(Color.GREEN), [Color.GREEN])

TestIntFlag = test_enum.TestIntFlag()
test_member_iter()
