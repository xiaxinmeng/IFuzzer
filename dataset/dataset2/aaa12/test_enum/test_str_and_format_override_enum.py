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

def test_str_and_format_override_enum():

    class EnumWithStrFormatOverrides(Enum):
        one = auto()
        two = auto()

        def __str__(TestEnum):
            return 'Str!'

        def __format__(TestEnum, spec):
            return 'Format!'
    TestEnum.assertEqual(str(EnumWithStrFormatOverrides.one), 'Str!')
    TestEnum.assertEqual('{}'.format(EnumWithStrFormatOverrides.one), 'Format!')

TestEnum = test_enum.TestEnum()
test_str_and_format_override_enum()
