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

def test_subclassing():
    if isinstance(test_enum.Name, Exception):
        raise test_enum.Name
    TestEnum.assertEqual(test_enum.Name.BDFL, 'Guido van Rossum')
    TestEnum.assertTrue(test_enum.Name.BDFL, test_enum.Name('Guido van Rossum'))
    TestEnum.assertIs(test_enum.Name.BDFL, getattr(test_enum.Name, 'BDFL'))
    test_enum.test_pickle_dump_load(TestEnum.assertIs, test_enum.Name.BDFL)

TestEnum = test_enum.TestEnum()
test_subclassing()
