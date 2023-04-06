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

def test_intenum_transitivity():

    class number(test_enum.IntEnum):
        one = 1
        two = 2
        three = 3

    class numero(test_enum.IntEnum):
        uno = 1
        dos = 2
        tres = 3
    TestEnum.assertEqual(number.one, numero.uno)
    TestEnum.assertEqual(number.two, numero.dos)
    TestEnum.assertEqual(number.three, numero.tres)

TestEnum = test_enum.TestEnum()
test_intenum_transitivity()
