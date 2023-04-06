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

def test_string_enum():

    class SkillLevel(str, Enum):
        master = 'what is the sound of one hand clapping?'
        journeyman = 'why did the chicken cross the road?'
        apprentice = 'knock, knock!'
    TestEnum.assertEqual(SkillLevel.apprentice, 'knock, knock!')

TestEnum = test_enum.TestEnum()
test_string_enum()
