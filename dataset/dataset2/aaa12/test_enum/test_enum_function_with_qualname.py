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

def test_enum_function_with_qualname():
    if isinstance(test_enum.Theory, Exception):
        raise test_enum.Theory
    TestEnum.assertEqual(test_enum.Theory.__qualname__, 'spanish_inquisition')

TestEnum = test_enum.TestEnum()
test_enum_function_with_qualname()
