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

def test_subclass_duplicate_name_dynamic():
    from types import DynamicClassAttribute

    class Base(Enum):

        @DynamicClassAttribute
        def test(TestEnum):
            return 'dynamic'

    class Test(Base):
        test = 1
    TestEnum.assertEqual(Test.test.test, 'dynamic')

TestEnum = test_enum.TestEnum()
test_subclass_duplicate_name_dynamic()
