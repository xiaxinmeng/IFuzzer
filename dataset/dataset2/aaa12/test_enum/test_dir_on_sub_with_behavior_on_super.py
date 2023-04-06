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

def test_dir_on_sub_with_behavior_on_super():

    class SuperEnum(Enum):

        def invisible(TestEnum):
            return 'did you see me?'

    class SubEnum(SuperEnum):
        sample = 5
    TestEnum.assertEqual(set(dir(SubEnum.sample)), set(['__class__', '__doc__', '__module__', 'name', 'value', 'invisible']))

TestEnum = test_enum.TestEnum()
TestEnum.setUp()
test_dir_on_sub_with_behavior_on_super()
