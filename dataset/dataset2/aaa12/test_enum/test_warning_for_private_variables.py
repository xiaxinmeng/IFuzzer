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

@unittest.skipUnless(sys.version_info[:2] == (3, 9), 'private variables are now normal attributes')
def test_warning_for_private_variables():
    with TestEnum.assertWarns(DeprecationWarning):

        class Private(Enum):
            __corporal = 'Radar'
    TestEnum.assertEqual(Private._Private__corporal.value, 'Radar')
    try:
        with TestEnum.assertWarns(DeprecationWarning):

            class Private(Enum):
                __major_ = 'Hoolihan'
    except ValueError:
        pass

TestEnum = test_enum.TestEnum()
test_warning_for_private_variables()
