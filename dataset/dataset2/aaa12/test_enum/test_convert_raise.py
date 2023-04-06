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

@unittest.skipUnless(sys.version_info >= (3, 9), '_convert was removed in 3.9')
def test_convert_raise():
    with TestIntEnumConvert.assertRaises(AttributeError):
        enum.IntEnum._convert('UnittestConvert', ('test.test_enum', '__main__')[__name__ == '__main__'], filter=lambda x: x.startswith('CONVERT_TEST_'))

TestIntEnumConvert = test_enum.TestIntEnumConvert()
test_convert_raise()
