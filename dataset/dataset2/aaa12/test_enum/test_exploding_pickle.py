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

def test_exploding_pickle():
    BadPickle = Enum('BadPickle', 'dill sweet bread-n-butter', module=__name__)
    globals()['BadPickle'] = BadPickle
    enum._make_class_unpicklable(BadPickle)
    test_enum.test_pickle_exception(TestEnum.assertRaises, TypeError, BadPickle.dill)
    test_enum.test_pickle_exception(TestEnum.assertRaises, PicklingError, BadPickle)

TestEnum = test_enum.TestEnum()
test_exploding_pickle()
