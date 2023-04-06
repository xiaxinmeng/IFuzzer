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

def test_format_override_mixin():

    class TestFloat(float, Enum):
        one = 1.0
        two = 2.0

        def __format__(TestEnum, spec):
            return 'TestFloat success!'
    TestEnum.assertEqual(str(TestFloat.one), 'TestFloat.one')
    TestEnum.assertEqual('{}'.format(TestFloat.one), 'TestFloat success!')

TestEnum = test_enum.TestEnum()
test_format_override_mixin()
