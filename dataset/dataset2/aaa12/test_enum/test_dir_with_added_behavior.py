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

def test_dir_with_added_behavior():

    class Test(Enum):
        this = 'that'
        these = 'those'

        def wowser(TestEnum):
            return "Wowser! I'm %s!" % TestEnum.name
    TestEnum.assertEqual(set(dir(Test)), set(['__class__', '__doc__', '__members__', '__module__', 'this', 'these']))
    TestEnum.assertEqual(set(dir(Test.this)), set(['__class__', '__doc__', '__module__', 'name', 'value', 'wowser']))

TestEnum = test_enum.TestEnum()
test_dir_with_added_behavior()
