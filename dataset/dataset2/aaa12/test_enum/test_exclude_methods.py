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

def test_exclude_methods():

    class whatever(Enum):
        this = 'that'
        these = 'those'

        def really(TestEnum):
            return 'no, not %s' % TestEnum.value
    TestEnum.assertIsNot(type(whatever.really), whatever)
    TestEnum.assertEqual(whatever.this.really(), 'no, not that')

TestEnum = test_enum.TestEnum()
test_exclude_methods()
