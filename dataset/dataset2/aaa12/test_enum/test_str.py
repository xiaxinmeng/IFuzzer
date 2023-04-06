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

def test_str():
    Perm = TestIntFlag.Perm
    TestIntFlag.assertEqual(str(Perm.R), 'Perm.R')
    TestIntFlag.assertEqual(str(Perm.W), 'Perm.W')
    TestIntFlag.assertEqual(str(Perm.X), 'Perm.X')
    TestIntFlag.assertEqual(str(Perm.R | Perm.W), 'Perm.R|W')
    TestIntFlag.assertEqual(str(Perm.R | Perm.W | Perm.X), 'Perm.R|W|X')
    TestIntFlag.assertEqual(str(Perm.R | 8), 'Perm.8|R')
    TestIntFlag.assertEqual(str(Perm(0)), 'Perm.0')
    TestIntFlag.assertEqual(str(Perm(8)), 'Perm.8')
    TestIntFlag.assertEqual(str(~Perm.R), 'Perm.W|X')
    TestIntFlag.assertEqual(str(~Perm.W), 'Perm.R|X')
    TestIntFlag.assertEqual(str(~Perm.X), 'Perm.R|W')
    TestIntFlag.assertEqual(str(~(Perm.R | Perm.W)), 'Perm.X')
    TestIntFlag.assertEqual(str(~(Perm.R | Perm.W | Perm.X)), 'Perm.-8')
    TestIntFlag.assertEqual(str(~(Perm.R | 8)), 'Perm.W|X')
    TestIntFlag.assertEqual(str(Perm(~0)), 'Perm.R|W|X')
    TestIntFlag.assertEqual(str(Perm(~8)), 'Perm.R|W|X')
    Open = TestIntFlag.Open
    TestIntFlag.assertEqual(str(Open.RO), 'Open.RO')
    TestIntFlag.assertEqual(str(Open.WO), 'Open.WO')
    TestIntFlag.assertEqual(str(Open.AC), 'Open.AC')
    TestIntFlag.assertEqual(str(Open.RO | Open.CE), 'Open.CE')
    TestIntFlag.assertEqual(str(Open.WO | Open.CE), 'Open.CE|WO')
    TestIntFlag.assertEqual(str(Open(4)), 'Open.4')
    TestIntFlag.assertEqual(str(~Open.RO), 'Open.CE|AC|RW|WO')
    TestIntFlag.assertEqual(str(~Open.WO), 'Open.CE|RW')
    TestIntFlag.assertEqual(str(~Open.AC), 'Open.CE')
    TestIntFlag.assertEqual(str(~(Open.RO | Open.CE)), 'Open.AC|RW|WO')
    TestIntFlag.assertEqual(str(~(Open.WO | Open.CE)), 'Open.RW')
    TestIntFlag.assertEqual(str(Open(~4)), 'Open.CE|AC|RW|WO')

TestIntFlag = test_enum.TestIntFlag()
test_str()
