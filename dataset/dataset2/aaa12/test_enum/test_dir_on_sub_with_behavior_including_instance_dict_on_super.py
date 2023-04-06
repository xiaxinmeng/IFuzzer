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

def test_dir_on_sub_with_behavior_including_instance_dict_on_super():

    class SuperEnum(IntEnum):

        def __new__(cls, value, description=''):
            obj = int.__new__(cls, value)
            obj._value_ = value
            obj.description = description
            return obj

    class SubEnum(SuperEnum):
        sample = 5
    TestEnum.assertTrue({'description'} <= set(dir(SubEnum.sample)))

TestEnum = test_enum.TestEnum()
TestEnum.setUp()
test_dir_on_sub_with_behavior_including_instance_dict_on_super()
