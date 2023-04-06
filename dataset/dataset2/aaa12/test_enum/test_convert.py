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

def test_convert():
    test_type = enum.IntEnum._convert_('UnittestConvert', ('test.test_enum', '__main__')[__name__ == '__main__'], filter=lambda x: x.startswith('CONVERT_TEST_'))
    TestIntEnumConvert.assertEqual(test_type.CONVERT_TEST_NAME_F, test_type.CONVERT_TEST_NAME_A)
    TestIntEnumConvert.assertEqual(test_type.CONVERT_TEST_NAME_B, 5)
    TestIntEnumConvert.assertEqual(test_type.CONVERT_TEST_NAME_C, 5)
    TestIntEnumConvert.assertEqual(test_type.CONVERT_TEST_NAME_D, 5)
    TestIntEnumConvert.assertEqual(test_type.CONVERT_TEST_NAME_E, 5)
    TestIntEnumConvert.assertEqual([name for name in dir(test_type) if name[0:2] not in ('CO', '__')], [], msg='Names other than CONVERT_TEST_* found.')

TestIntEnumConvert = test_enum.TestIntEnumConvert()
TestIntEnumConvert.setUp()
test_convert()
