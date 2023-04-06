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

def test_repr():
    Perm = TestIntFlag.Perm
    TestIntFlag.assertEqual(repr(Perm.R), '<Perm.R: 4>')
    TestIntFlag.assertEqual(repr(Perm.W), '<Perm.W: 2>')
    TestIntFlag.assertEqual(repr(Perm.X), '<Perm.X: 1>')
    TestIntFlag.assertEqual(repr(Perm.R | Perm.W), '<Perm.R|W: 6>')
    TestIntFlag.assertEqual(repr(Perm.R | Perm.W | Perm.X), '<Perm.R|W|X: 7>')
    TestIntFlag.assertEqual(repr(Perm.R | 8), '<Perm.8|R: 12>')
    TestIntFlag.assertEqual(repr(Perm(0)), '<Perm.0: 0>')
    TestIntFlag.assertEqual(repr(Perm(8)), '<Perm.8: 8>')
    TestIntFlag.assertEqual(repr(~Perm.R), '<Perm.W|X: -5>')
    TestIntFlag.assertEqual(repr(~Perm.W), '<Perm.R|X: -3>')
    TestIntFlag.assertEqual(repr(~Perm.X), '<Perm.R|W: -2>')
    TestIntFlag.assertEqual(repr(~(Perm.R | Perm.W)), '<Perm.X: -7>')
    TestIntFlag.assertEqual(repr(~(Perm.R | Perm.W | Perm.X)), '<Perm.-8: -8>')
    TestIntFlag.assertEqual(repr(~(Perm.R | 8)), '<Perm.W|X: -13>')
    TestIntFlag.assertEqual(repr(Perm(~0)), '<Perm.R|W|X: -1>')
    TestIntFlag.assertEqual(repr(Perm(~8)), '<Perm.R|W|X: -9>')
    Open = TestIntFlag.Open
    TestIntFlag.assertEqual(repr(Open.RO), '<Open.RO: 0>')
    TestIntFlag.assertEqual(repr(Open.WO), '<Open.WO: 1>')
    TestIntFlag.assertEqual(repr(Open.AC), '<Open.AC: 3>')
    TestIntFlag.assertEqual(repr(Open.RO | Open.CE), '<Open.CE: 524288>')
    TestIntFlag.assertEqual(repr(Open.WO | Open.CE), '<Open.CE|WO: 524289>')
    TestIntFlag.assertEqual(repr(Open(4)), '<Open.4: 4>')
    TestIntFlag.assertEqual(repr(~Open.RO), '<Open.CE|AC|RW|WO: -1>')
    TestIntFlag.assertEqual(repr(~Open.WO), '<Open.CE|RW: -2>')
    TestIntFlag.assertEqual(repr(~Open.AC), '<Open.CE: -4>')
    TestIntFlag.assertEqual(repr(~(Open.RO | Open.CE)), '<Open.AC|RW|WO: -524289>')
    TestIntFlag.assertEqual(repr(~(Open.WO | Open.CE)), '<Open.RW: -524290>')
    TestIntFlag.assertEqual(repr(Open(~4)), '<Open.CE|AC|RW|WO: -5>')

TestIntFlag = test_enum.TestIntFlag()
test_repr()
